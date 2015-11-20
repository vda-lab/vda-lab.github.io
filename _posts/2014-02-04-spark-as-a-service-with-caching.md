---
layout: post
title:  "Spark as a service with caching"
date:   2014-02-04 21:11
author: Toni Verbeiren
categories: main
published: false
tags:
- spark
---
Today, I've come a little closer to what in my opinion is currently the state-of-the art approach to analytics of big data set, especially visual analytics.

The data is stored on disk to start with. It can be a file on the local disk or a file server, but it can be a file on a Hadoop cluster as well. The latter is the best approach because we will be interested in distributing not only the files, but also the computation.

[Spark](http://homes.esat.kuleuven.be/~bioiuser/blog/?p=66) is then used to load the data and run parallel algorithms on this data. We [used this approach earlier](/2014/01/a-d3-visualization-from-spark-as-a-service) for a visual analytics prototype using [Processing](http://processing.org/) as a frontend. This method, however, statically combines all the different layers in the analysis. This has some drawbacks: First changing something to the visualisation requires a recompile and a rerun of the full program, including the Spark-specific code. Secondly, a different visualisation or an alternative encoding has to be compiled-in completely and can not share the same Spark (cached) instances. In other words, although the components can be reused, they have to be deployed as a whole which leads to a number of copies of the same data and algorithms.

That is the reason why we looked at the [Spark Jobserver](/2014/01/spark-as-a-service). We created a prototype already where the data resides in Spark and is queried using a REST API that runs Spark underneath to do its magic. The result is a JSON stream that can be handled for instance in a browser and visualised using any Javascript visualisation library. We choose [D3.js](http://d3js.org/).

What was still lacking was the fact that I could not share state (for instance a cached instance of a dataset) across different runs of the REST call. The [previous example](/2014/01/a-d3-visualization-from-spark-as-a-service) only works in a static way or in other words, there are no options to the REST POST request that define the query.

This, however, had to be possible when reading the [Readme](https://github.com/ooyala/incubator-spark/blob/jobserver-preview-2013-12/jobserver/README.md) file of the [jobserver project](https://github.com/ooyala/incubator-spark/tree/jobserver-preview-2013-12/jobserver/) on GitHub. After some fiddling around and looking at the code, I got it working. There are two class files, one for setting up the SparkContext (and caching the required dataset), the other for querying some specific part of it. Note that in the following code, input handling is poorly managed and not yet checked for errors.

{% highlight scala %}
object TFs extends SparkJob {

  def main(args: Array[String]) {

  }

  // TODO !
  override def validate(sc: SparkContext, config: Config): SparkJobValidation = SparkJobValid

  override def runJob(sc: SparkContext, config: Config): Any = {

    val p = config.getString("input.string").split(" ").toList

    // Parsing and conversion to tuples
    val bed = sc.textFile("/Users/toni/Dropbox/_KUL/_data/201101_encode_motifs_in_tf_peaks.bed")
    val bedArray = bed.map(_.split("\\s+")).map(x =&gt; extractFeatures(x))
    val cachedRdd = bedArray.cache()

    // force evaluation
    val evaluation = cachedRdd.count()

    // return info about the cached RDD as map
    sc.getPersistentRDDs

  }

  def extractFeatures(line: Array[String]): (String, Int, Int, String) = {
    (line(0).toString, line(1).toInt, line(2).toInt, line(3).toString)
  }
}
{% endhighlight %}

The query class looks similar in almost any aspect, except the runJob method:

{% highlight scala %}
override def runJob(sc: SparkContext, config: Config): Any = {

// Parameters, we expect in order:
// - number of RDD to reuse
// - chromosome
// - start position
// - end position
// - optional: TF
val p = config.getString("input.string").split(" ").toList

// a map with the persistent RDDs
val listOfPersistentRDDs = sc.getPersistentRDDs

val myRDD = p(0).toInt
val chr = p(1).toString
val b = p(2).toInt
val e = p(3).toInt
// val tf = ...

val myCachedRdd = listOfPersistentRDDs(myRDD).asInstanceOf[RDD[(String, Int, Int, String)]]

myCachedRdd.filter(x =&gt; (x._1 == chr) && (x._2 &gt;= b) && (x._3 &lt;= e)).collect().toList

}
{% endhighlight %}

The magic happens by means of two mechanisms:

  1. The Job Server makes sure that the SparkContext keeps running (if we choose it to)
  1. The ID for the RDD with the cached data is passed from one object/class to the other one by means of the input.string parameter at runtime.

To make things clear, this is the procedure to actually do a query. I assume that the two classes are compiled and assembled into the correct JAR file (here `spark-job-server_2.9.3-0.9.0-incubating-SNAPSHOT-test.jarz).

{% highlight sh %}
curl --data-binary @jobserver/target/scala-2.9.3/spark-job-server_2.9.3-0.9.0-incubating-SNAPSHOT-test.jar localhost:8090/jars/TFs
curl -d "" 'localhost:8090/contexts/my_context'
url -d "" 'localhost:8090/jobs?appName=TFs&classPath=spark.jobserver.TFs&context=my_context'
{% endhighlight %}

This returns the job ID in the JSNON output:

{% highlight json %}
{
  "status": "STARTED",
  "result": {
    "jobId": "4ada143e-2dfe-412e-b878-ad0b38d73a8f",
    "context": "my_context"
  }
}
{% endhighlight %}

We can query this job:
{% highlight sh %}
curl 'localhost:8090/jobs/4ada143e-2dfe-412e-b878-ad0b38d73a8f'
{% endhighlight %}

This yields:

{% highlight json %}
{
  "status": "OK",
  "result": {
    "12": "MappedRDD[12] at map at TFs.scala:27",
    "3": "MappedRDD[3] at map at TFs.scala:27"
  }
}
{% endhighlight %}

We want the last one, note the number. It is the first option on the line. The other options are the chromosome we are interested in and the start and end position:

{% highlight sh %}
curl -d "input.string = 12 chr1 1000 100000" 'localhost:8090/jobs?appName=TFs&classPath=spark.jobserver.TFQuery&context=my_context&sync=true'
{% endhighlight %}

The result:
{% highlight json %}
{
  "status": "OK",
  "result": [["chr1", 29386, 29397, "Ets"], ["chr1", 29389, 29400, "Ets"]]
}
{% endhighlight %}

I now have a query service. Keep the RDD number the same and change the options. By the way, it is *blazingly* fast!

Please note that the second query immediately gives the result back. This is due to the `sync=true` option in the REST Call. Why didn't we do that the first time when loading the data in memory?

You can, but then an internal timeout will result in a job that finishes before the data is actually read and cached. This makes sense, because it is one of the reasons this approach is valuable: split the tasks that take time from those that do not.

Please note that anyone can upload JAR files to the server, create a context or reuse an existing one. In other words, this really is Spark as a service, not only for *my* visualisation project but for a team working on the same or similar data workflows.

Now, imagine we augment the Adam tool with a web interface like the above?!      
