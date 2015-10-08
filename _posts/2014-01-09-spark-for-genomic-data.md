---
layout: post
title:  "Spark for Genomic Data"
date:   2014-01-09 18:03:00
author: Toni Verbeiren
categories: spark shark scala
tags:
- spark
- shark
- scala
---
We have been researching the use of [Spark](http://spark.incubator.apache.org/) and/or [Shark](https://github.com/amplab/shark/wiki) as a backend for our visualisation projects. If you are not familiar with Spark, please [take a look here](http://spark.incubator.apache.org/screencasts/1-first-steps-with-spark.html).
In short: Spark is a platform for distributed handling of data. Think of [Hadoop](http://hadoop.apache.org/) but allowing for interactive rather than batch use. One of the first things we considered is whether to start of using Spark or rather Shark, which is based on it but offers a SQL like syntax instead of a Scala/Python/Java API. But first a word about the data and about the use of Spark to handle the data.

# Data

[![BED file sample]({{ site.baseurl }}/assets/occurrence_transcription-factors_small.png)]({{ site.baseurl }}/assets/occurrence_transcription-factors_large.png)

We use a [BED](https://genome.ucsc.edu/FAQ/FAQformat.html#format1) file as input format and took [this one](ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase1/analysis_results/functional_annotation/annotation_sets/201101_encode_motifs_in_tf_peaks.bed.gz) to start with. It contains information on [transcription factors](http://en.wikipedia.org/wiki/Transcription_factor) and where they bind on the genome. This input format is a text file and can easily be parsed.

## Parsing the data
We started by exploring the Scala interface to Spark, first from the REPL which allows for interactive exploring of the API.

The main benefits of using the Scala interface are the following:

* No additional dependencies required
* All flexibility of Scala as a powerful language, byte-compatible with Java

Reading in the data and parsing it can easily be done:

{% highlight scala %}
val bed = sc.textFile("201101_encode_motifs_in_tf_peaks.bed")
val bedArray = bed.map(_.split("\\s+"))
{% endhighlight %}

This does not *do* anything yet. The method `collect()` gets the data out of the RDD structure and return an Array. The first element from the dataset can be selected using:

{% highlight scala %}
>scala&gt; bedArray take 1
...
res1: Array[Array[java.lang.String]] = Array(Array(chr1, 29386, 29397, Ets, ., -))
{% endhighlight %}

Please note that by default RDDs contains `Array[Array[String]]` which makes it hard to extract the numbers and work with them. In order to convert *one line* of our data to a quadruple, we define the following function and add it as a transformation:

{% highlight scala %}
def extractFeatures(line: Array[String]): (String, Int, Int, String) = {
  (line(0).toString, line(1).toInt, line(2).toInt, line(3).toString)
}
val bedArray = bed.map(_.split("\\s+")).map(x =&gt; extractFeatures(x))
{% endhighlight %}

So that we can easily filter:

{% highlight scala %}
val result = bedArray filter(x =&gt; (x._1 == "chr4" && x._3 &gt; 190930000 && x._2 &lt; 190940000))
{% endhighlight %}

It would also be possible to define a class that mirrors the data and read the data into an object of that class for easier access and development.

A very important aspect of Spark is the possibility to cache intermediate steps in order to retrieve them faster:

{% highlight scala %}
val cached = bedArray.cache()
val result = cached filter(x =&gt; (x._1 == "chr4" && x._3 &gt; 190930000 && x._2 &lt; 190940000))
{% endhighlight %}

# Discussion

The Spark framework does what it needs to do: it abstracts away everything that has to do with running code in parallel on a cluster by providing a <em>functional</em> API in Scala (as well as Python and Java).

In a later post, we will take a look at Shark and see how it compares to Spark and which one may be more applicable to our use-case.

# Learning resources
Please refer to this pages for more information about Spark:

* [http://ampcamp.berkeley.edu/big-data-mini-course/](http://ampcamp.berkeley.edu/big-data-mini-course/)
* [http://ampcamp.berkeley.edu/amp-camp-two-strata-2013/](http://ampcamp.berkeley.edu/amp-camp-two-strata-2013/)
