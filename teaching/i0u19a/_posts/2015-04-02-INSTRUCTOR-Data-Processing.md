---
title: Instructor notes on Data Processing
layout: page
instructor: "true"
---

# 1. Word Count and Beyond:

Remember:

	cat easy_file.txt | ./mapper.py | sort -k 1,1 | ./reducer.py


## 1.1 Hadoop streaming Word Count

```bash
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-0.20.2-cdh3u6.jar \
  -mapper mapper.py \
  -reducer reducer.py \
  -input /mnt/bioinformatics_leuven/i0u19a/data/drugdb/AMM_det_H.csv \
  -output output \
```

Issue: `mapper.py` assumes tab-delimited data, but `AMM_det_H.csv` is comma-separated.


## 1.2 CSV parsing

```bash
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-0.20.2-cdh3u6.jar \
  -mapper mapper1.py \
  -reducer reducer.py \
  -input /mnt/bioinformatics_leuven/i0u19a/data/drugdb/AMM_det_H.csv \
  -output output \
```

Paracetamol: Look in the dataset (less) and find the word. The answer is 136.



## 1.3 Selective parsing

```bash
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-0.20.2-cdh3u6.jar \
  -mapper mapper2.py \
  -reducer reducer.py \
  -input /mnt/bioinformatics_leuven/i0u19a/data/drugdb/AMM_det_H.csv \
  -output output \
```

The most active substance? This is the top-10:

    cat  part-00000  | sort -r -g -k2,2 -t$'\t' | head


## 1.4 Active substances and maximum dose

```bash
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-0.20.2-cdh3u6.jar \
  -mapper mapper3.py \
  -reducer reducer3.py \
  -input /mnt/bioinformatics_leuven/i0u19a/data/drugdb/AMM_det_H.csv \
  -output output \
```

This is a poor way to pass additional data between two phases. We could use different approaches: `JSON`, ... Another option would be to use a datamodel and work with objects. These objects then need to be converted to a stream of data.


# 2. Normalization and Joins

```bash
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-0.20.2-cdh3u6.jar \
  -mapper mapperJoin.py \
  -reducer reducerJoin.py \
  -input mapper.py \
  -output output \
```

The `-input` flag is strange and is actually a dummy file as the real input files are defined in the mapper. Be careful, this would not work as-as on HDFS.

To get a sorted listing:

    cat  part-00000  | sort -r -g -k2,2 -t$'\t' | head


# 3. Spark


```python
file = sc.textFile("/mnt/bioinformatics_leuven/i0u19a/data/drugdb/AMM_det_H.csv")
counts = file.flatMap(lambda line: line.split(",")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
sorted = counts.map(lambda x: (x[1],x[0]) ).sortByKey(False)
```

Top-10

    sorted.take(10)

Paracetamol:

    sorted.filter(lambda x: x[1]=='"PARACETAMOL"').collect()

```
result2 = file.map(lambda line: line.split(",")) \
    .map(lambda x: x[2]) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)
result2.filter(lambda x: x[0] == '"PARACETAMOL"')
```


