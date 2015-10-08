---
layout: post
title:  "Spark as a service"
date:   2014-01-29 14:46
author: Toni Verbeiren
categories: spark
tags:
- spark
---
As mentioned earlier on this blog, we are using Spark as a backend for our data processing. In our earlier work, we tied [Processing](http://processing.org/) and [Spark](http://homes.esat.kuleuven.be/~bioiuser/blog/?p=66) together by an intermediate layer that constitutes of a [lazy tree zipper data structure](/2014/01/lazy-functional-tree-zipper-for-zoom-levels) to represent the different zoom levels in our data.

This approach has one big disadvantage: all code is tied together in a single set of classes and objects. Although largely functional in nature (except for the visualisation part using Processing), it is not a very scalable solution.

Another approach would be to present Spark as a service and connect to it via [REST calls](http://en.wikipedia.org/wiki/Representational_state_transfer). Luckily, the guys from [Ooyala](http://www.ooyala.com/) have made available [an extension to Spark](https://github.com/ooyala/incubator-spark/tree/jobserver-preview-2013-12/jobserver#wordcountexample-walk-through) that allows for just that. In this post, we experiment with the service. In a later post, we will create a visualisation based on it.

# Installation
The installation instructions can be found [here](http://gethue.tumblr.com/post/71963991256/a-new-spark-web-ui-spark-app), although we need only a subset of these instructions. First, download from GitHub:

{% highlight sh %}
git clone https://github.com/ooyala/incubator-spark.git spark-server
cd spark-server
git checkout -b jobserver-preview-2013-12 origin/jobserver-preview-2013-12
{% endhighlight %}

Then, compile:
{% highlight sh %}
sbt/sbt
project jobserver
re-start
{% endhighlight %}

This launches the jobserver to listen on port 8090 by default. Please note that the first command starts `sbt` (the Scala Build Tool), the other two are `sbt` *tasks*.

# Our first genome service
In order to test it, we can use [the built-in test](https://github.com/ooyala/incubator-spark/tree/jobserver-preview-2013-12/jobserver#wordcountexample-walk-through) or create one of our own.

We changed the existing word count test file into:
{% highlight scala %}
package spark.jobserver

import com.typesafe.config.{Config, ConfigFactory}
import org.apache.spark._
import org.apache.spark.SparkContext._
import scala.util.Try

object TransFactors extends SparkJob {

  def main(args: Array[String]) {

  val sc = new SparkContext("local[4]", "TransFactors")
    val config = ConfigFactory.parseString("")
    val results = runJob(sc, config)
    println("Result is " + results)
  }

  override def validate(sc: SparkContext, config: Config): SparkJobValidation = SparkJobValid

  override def runJob(sc: SparkContext, config: Config): Any = {
    val bed = sc.textFile("201101_encode_motifs_in_tf_peaks.bed")
    val bedArray = bed.map(_.split("\\s+")).map(x =&gt; extractFeatures(x))
    val keyValue = bedArray.map(x =&gt; ((x._1,x._4),1))
    val pivot = keyValue.countByKey()

    pivot.map(x=&gt;(x._1._1,x._1._2,x._2)).toList

  }

  def extractFeatures(line: Array[String]): (String, Int, Int, String) = {
    (line(0).toString, line(1).toInt, line(2).toInt, line(3).toString)
  }
}
{% endhighlight %}

We use the same example file as [before](/2014/01/spark-for-genomic-data). Please note that error handling is avoided by always returning `SparkJobValid` as a result of the validation step. Also note that this is very simple service that does not take arguments (yet).

The `runJob` method results in a `List` that represents the triple: `(Chromosome, TranscriptionFactor, frequency)`.

Compiling can be done using `sbt`, after which we restart the job server:
{% highlight sh %}
jobserver/test:package
re-start
{% endhighlight %}

Interacting with the job server can be done using, e.g. `curl`. We first deploy our code for handling requests:
```
curl --data-binary @jobserver/target/scala-2.9.3/spark-job-server_2.9.3-0.9.0-incubating-SNAPSHOT-test.jar localhost:8090/jars/test
```
Please note that you might have to adapt that for your local Scala and Spark version.

Almost ready... We can now query our job server using the following `POST` request:
```
curl -d "" 'localhost:8090/jobs?appName=test&classPath=spark.jobserver.TransFactors&sync=true'
```

In the request, we specify that we want to wait for the result (`sync=true`). The result is a `JSON` file with two fields: `status` and `result`.

# Interacting with the Spark job server
The full API [is explained here](https://github.com/ooyala/incubator-spark/tree/jobserver-preview-2013-12/jobserver#api). It allows to create Spark Contexts, start jobs (a)synchronously, query jobs, etc. In a followup post, I will describe how the Spark job server can be used to act as a backend for the visualisations.
