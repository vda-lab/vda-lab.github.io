---
title: Data Processing Exercises
layout: page
---

## Preparation
Download the file `i0u19a-processing.tar.gz` using `wget http://vda-lab.be/teaching/i0u19a/assets/i0u19a-processing.tar.gz` in your home directory. Unpack them using `tar -xvzf i0u19-processing.tar.gz`.

#### Preparation by teachers
* Get hadoop system running, e.g. `docker run -v /Users/jaerts/Google\ Drive/Teaching/I0U19A/ExerciseMaterial:/home/i0u19a -it --rm sequenceiq/hadoop-docker:2.7.0 /etc/bootstrap.sh -bash`
* Get pyspark running, e.g. `docker run -d -p 8888:8888 jupyter/pyspark-notebook` (see https://github.com/jupyter/docker-stacks/tree/master/pyspark-notebook)

**Note to Jan & Thomas: solution files are hidden**

## Bigger picture
We will use the beers dataset for the exercises in this session.

The beer dataset looks like this:
<pre>
,make,type,alcoholpercentage,brewery
1,3 Schténg,hoge gisting,6,Brasserie Grain d'Orge
2,400,blond,5.6,'t Hofbrouwerijke voor Brouwerij Montaigu
3,IV Saison,saison,6.5,Brasserie de Jandrain-Jandrenouille
4,V Cense,hoge gisting;special belge,7.5,Brasserie de Jandrain-Jandrenouille
5,VI Wheat,hoge gisting;tarwebier,6,Brasserie de Jandrain-Jandrenouille
6,Aardmonnik,oud bruin,8,De Struise Brouwers
7,Aarschotse Bruine,bruin,6,Stadsbrouwerij Aarschot
8,Abbay d'Aulne Blonde des Pères 6,abdijbier;blond,6,Brasserie Val de Sambre
9,Abbay d'Aulne Brune des Pères 6,abdijbier;bruin,6,Brasserie Val de Sambre
</pre>

Using the beer dataset (see [http://vda-lab.be/teaching/i0u19a/datasets.html]({{ site.baseurl }}/teaching/i0u19a/datasets.html)), we  want to find out the following things:

* How many beers are there for each alcoholpercentage?
* Which are the 5 breweries with the highest average alcoholpercentage?
* Which are the 5 breweries with the most types of beer? And what are these types? (**note to self: to use json as value**)

There are different ways of doing this. We will (a) first just write a mapper and reducer script and run these in a pipe on the command line, (b) then run the same scripts using Hadoop, and (c) redo the same using Spark.

## A. How many beers are there for each alcoholpercentage?
### A.1 Mapper and reducer on the linux command line
Take the scripts `mapper1.py` and `reducer1.py`, and edit the indicated lines. Output from `cat beers.csv | ./mapper1.py` should look like this:

<pre>
6     1
5.6   1
6.5   1
7.5   1
6     1
8     1
6     1
6     1
6     1
...
</pre>

Output from running `cat beers.csv | ./mapper1.py | sort | ./reducer1.py` should look like this:
<pre>
0     1
0.25  2
0.3   1
0.4   1
0.5   3
1     1
1.2   2
1.3   1
1.4   2
1.5   8
...
</pre>

Running the mapper and reducer piped together (but including the `sort`!) is an easy way to check if your scripts do what they need to do, before you want to run these on a Hadoop cluster (see below).

#### Question
Which alcoholpercentage is the most common?

### A.2 Mapper and reducer using Hadoop
Instead of running a complete cluster of machines, we will run Hadoop in "single-node" mode. This means that we can use and test any functionality we need, but it will be slow. After all, instead of just running the pipe as before, we will have the overhead of the Hadoop system without being able to split the work across machines.

The `hadoop` command contains several subcommands, such as `hadoop fs` and `hadoop jar` (which we'll touch upon).

To run anything using Hadoop, we need to **put all necessary files on the Hadoop Distributed File System (HDFS)**.

<pre>
hadoop fs -put mapper1.py
hadoop fs -put reducer1.py
hadoop fs -put beers.csv
</pre>

If we were working on a large Hadoop cluster, this would split each file into chunks and distribute them among the different machines. In our case, it will all remain on our current machine, but moved into the Hadoop system. Use `hadoop fs -ls` to check if the files are copied to HDFS.

In order to run this map-reduce pipeline using hadoop, we will run the `hadoop` command with the `jar` subcommand. The "jar"-name refers to the file extension used for a java program. The java program we will run is one that takes a mapper and reducer, and sends a data file through them (= hadoop streaming). Other arguments necessary are: which file contains the mapper code, which file contains the reducer code, where should the output be stored, and which files need to be imported.

<pre>
hadoop jar \
 /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.0.jar \
 -mapper "python mapper1.py" \
 -reducer "python reducer.py" \
 -input beers.csv \
 -output OutputDir \
 -file mapper1.py \
 -file reducer1.py \
 -file beers.csv
</pre>

Starting this command will send a lot of information to the screen:
<pre>
16/03/29 03:54:27 INFO client.RMProxy: Connecting to ResourceManager at /0.0.0.0:8032
16/03/29 03:54:29 INFO input.FileInputFormat: Total input paths to process : 31
16/03/29 03:54:30 INFO mapreduce.JobSubmitter: number of splits:31
16/03/29 03:54:30 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1459237999031_0001
16/03/29 03:54:31 INFO impl.YarnClientImpl: Submitted application application_1459237999031_0001
16/03/29 03:54:31 INFO mapreduce.Job: The url to track the job: http://455083e722e3:8088/proxy/application_1459237999031_0001/
16/03/29 03:54:31 INFO mapreduce.Job: Running job: job_1459237999031_0001
16/03/29 03:54:42 INFO mapreduce.Job: Job job_1459237999031_0001 running in uber mode : false
16/03/29 03:54:42 INFO mapreduce.Job:  map 0% reduce 0%
16/03/29 03:55:20 INFO mapreduce.Job:  map 19% reduce 0%
...
</pre>

If everything works as it should, you should see a "Job completed successfully" somewhere.

We can now check if the output was generated: there should be a new folder on HDFS called `OutputDir`. It should show up with `hadoop fs -ls`. To list the files in that folder itself, run `hadoop fs -ls OutputDir`.

You'll see a file named `part-00000`. This is the actual output from your mapreduce job. In this particular example, there is only one output file. You can inspect the contents of that file while it's still on HDFS using e.g. `cat`: `hadoop fs -cat OutputDir/part-00000 | head `. To actually copy the file to your local filesystem, run `hadoop fs -getmerge OutputDir/ my-local-file.txt`.

#### Question
Do you get the same output as in A.1?

### A.3 Using Spark

**TO BE DONE**

## B. Which are the 5 breweries with the highest average alcoholpercentage?

**TO BE DONE**


## C. Which are the 5 breweries with the most types of beer? And what are these types?

**TO BE DONE**
