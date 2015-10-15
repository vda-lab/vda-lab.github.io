---
layout: post
title:  "Shark or spark"
date:   2014-01-29 10:03
author: Toni Verbeiren
categories: spark shark
tags:
- spark
- shark
---
In [a previous post](/2014/01/spark-for-genomic-data), we discussed the first steps into using Spark for analysing genomic data at scale. We now turn to Shark to see which one may be better suited for the task at hand.

## Introduction
[Shark](https://github.com/amplab/shark/wiki) is built on top of Spark and is similar to [Apache Hive](http://hive.apache.org/) in that it provides a SQL-like interface to the data: `HSQL`. As we will see, it may have some benefits, but also some disadvantages.

**Note**: had to increase the amount of memory available to the spark shell by adding the following to `shark-env.sh`: `-XX:MaxPermSize=512m`

## Shark to use
We first have to create the table:
{% highlight sql %}
CREATE TABLE genomea(chr STRING, lower BIGINT, upper BIGINT, annot STRING)
row format delimited
fields terminated by '\t';
{% endhighlight %}

Please note that we immediately specify the correct data types for the columns. Then adding the data to the table is a query away:

{% highlight sql %}
load data local inpath "201101_encode_motifs_in_tf_peaks.bed"
into table genomes;
{% endhighlight %}

Information on the data file and format used can be found [here](/2014/01/spark-for-genomic-data).

Queries can now be performed easily:
{% highlight sql %}
select * from genomes where chr == "chr4" and (upper &gt; 190930000 AND lower &lt; 190940000
{% endhighlight %}

Caching the data is done like this:

{% highlight sql %}
create table genomea_cached as select * from genomes;
{% endhighlight %}

## Shark as a service
Shark can easily be run as a service in order to access it, e.g., via `jdbc` from a script that is included in the installation. This enables any custom-built application to connect to it, effectively turning your data handling into a tiered architecture with lots of possibilities.

Shark can be called From the CLI:
{% highlight sh %}
bin/shark -e "SELECT * FROM genomes where chr == \"chr4\" and (upper > 190930000 AND lower < 190940000)"
{% endhighlight %}

## Benefits

At first sight, Shark seems to have some benefits over the default Scala interface to Spark.

First of all, rows have the correct data type because the tables are created as such. The SQL syntax enables a lot of people to get access to the data using the knowledge they already have. Especially, if you combine this with the fact that Shark can be exposed as a service out-of-the box.

Another possibility is to extend Shark with approximate queries. That is precisely what [BlinkDB](http://blinkdb.org/) is all about. It is based on Shark, but takes into account confidence intervals or response times.

## But...
There are is one main disadvantages to the Shark approach: This has to do with the flexibility. A SQL-like syntax is very nice, but the data needs to fit in a table structure. Not all data can easily be transformed to do that. Most data cleaning will have to be done before using Shark to expose the data to users. This means that we need other tools to pre-process the data, but then these other tools can possibly be used for querying as well?

A second disadvantages lies in the fact that one can not add a column to a table in
`HSQL`. This has to be done by creating a second table and joining the two into a third.

A smaller disadvantage may be that additional dependencies are introduced, especially when deploying BlinkDB.

## Calling Shark From Scala

It is possible to interface to Shark from Scala code:

{% highlight scala %}
val tst = sql2rdd("SELECT * FROM genomes where chr == \"chr4\" and (upper > 190930000 AND lower < 190940000)")
{% endhighlight %}

Something peculiar happens here, or not if you think about it. The result is wrapped in an array of type `Row`. This is a class that has getters for all the primitive types available to `HSQL`. Getting the data out requires some work. This is an example to get the data out in a comma-separated list:

{% highlight scala %}
tst foreach ( x =&gt; println(x.getString("chr") + "," + x.getLong("lower") + "," + x.getLong("upper") + "," + x.getString("annot")))
{% endhighlight %}

It can get a little easier for Strings and Ints, because `get` in itself is enough.

{% highlight scala %}
tst foreach ( x =&gt; println(x.get("chr") + "," + x.get("lower")))
{% endhighlight %}

In this case, however, the type is (the most general) `Object`. Only the specific getters return the correct type.

It all depends what one wants to do with the results afterwards. If one needs to write a `json` stream as a result, it does not matter.

At the recent Spark Summit, on one of the slides, the following code was mentioned:
{% highlight scala %}
val points = sc.runSql[Double,Double](“select latitude, longitude from historic_tweets")
{% endhighlight %}

This means that it *should* be possible to specify the types of the data to be read from the query. I’m not sure, however, that this method is already implemented and I haven't tried it out yet.

## Conclusion
For our work, we will be using Spark, not Shark. The benefits of Shark in our use-case do not outweigh the additional effort of transforming the data back and forth. Moreover, as will be discussed in a later post, we will see that Spark itself can be exposed in the form of a REST API, covering the most important advantage of Shark.

## Additional Info

* [https://github.com/amplab/shark/wiki/Running-Shark-Locally](https://github.com/amplab/shark/wiki/Running-Shark-Locally)
* [https://github.com/amplab/shark/wiki/Shark-User-Guide](https://github.com/amplab/shark/wiki/Shark-User-Guide)
*   <http://www.youtube.com/watch?v=w0Tisli7zn4>.

 [1]: http://homes.esat.kuleuven.be/~bioiuser/blog/?p=60
 [2]: https://github.com/amplab/shark/wiki
 [3]: http://hive.apache.org/
 [4]: http://blinkdb.org/
