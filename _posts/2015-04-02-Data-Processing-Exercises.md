---
title: Data Processing Exercises
layout: page
excerpt: This exercise session deals with map/reduce and related concepts.
---

## 1. Word count and beyond

### 1.1 Word count using Hadoop Streaming

Implement the Python `mapper` and `reducer` scripts on the slides of week 6. Run the Hadoop streaming API on the Amazon server. Use the data in 'AMM_det_H.csv' from the drugs dataset for this.

Mapper:

``` python
#!/usr/bin/env python

# Simple mapper, just like on the lecture slides
# Lines are split on spaces:
#  - good for word count
#  - not good for CSV or TSV files


import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print '%s\t%s' % (word, 1)
```

Reducer:

~~~python
#!/usr/bin/env python

# A simple reducer, as used in the lecture
# This reducer can be used for:
# - mapper.py: simple word count
# - mapper1.py: all columns are passed
# - mapper2.py: only active substances are passed

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s' % (current_word, current_count)
~~~

Make sure the scripts can be executed (`chmod u+x *.py` if needed).

To run this example in the shell (not Hadoop!)

~~~bash
cat /mnt/bioinformatics_leuven/i0u19a/data/drugdb/AMM_det_H.csv | ./mapper.py | sort -k 1,1 | ./reducer.py
~~~

We first have to set some environment variables in order for the rest to work properly:

~~~ bash
export PATH="$PATH:/mnt/bioinformatics_leuven/homes/tverbeiren/hadoop-common/hadoop-dist/target/hadoop-2.4.0/bin"
export JAVA_HOME="/usr/lib/jvm/java-7-openjdk-amd64/"
export PATH="$PATH:/opt/hadoop/hadoop-dist/target/hadoop-2.4.0/bin"
export PATH="$PATH:/opt/spark/bin"
export SPARK_HOME="/opt/spark"
~~~

To run the example using Hadoop, use the following:

~~~bash
hadoop jar /opt/hadoop/hadoop-tools/hadoop-streaming/target/hadoop-streaming-2.4.0.jar \
  -mapper mapper.py \
  -reducer reducer.py \
  -input /mnt/bioinformatics_leuven/i0u19a/data/drugdb/AMM_det_H.csv \
  -output output
~~~

Does this work? Does it give some insight? Why (not)?


### 1.2 Attempt 2

What about splitting the lines (in the mapper) on ',' instead of spaces? Adapt the `mapper.py` script. Name it `mapper1.py`. Do we have to change the reducer script?

Mapper:

~~~python
#!/usr/bin/env python

# Lines are split on ',':
#  - good for CSV files
# 'All' columns are passed to reduce phase


import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split(",")
    for word in words:
        print '%s\t%s' % (word, 1)
~~~

The reducer is the same.

Hadoop can be initiated like this:

~~~bash
hadoop jar /opt/hadoop/hadoop-tools/hadoop-streaming/target/hadoop-streaming-2.4.0.jar \
  -mapper mapper1.py \
  -reducer reducer.py \
  -input /mnt/bioinformatics_leuven/i0u19a/data/drugdb/AMM_det_H.csv \
  -output output
~~~

Does this work? Does it give some insight? Why (not)? How many times is PARACETAMOL the active substance?

In order to find Paracetamol: Look in the dataset (using for instance `less`) and find the word. The answer is 136.

What is the most used substance?

Please note that in order to effectively sort in a tab-delimited dataset, you need to the following:

    cat  part-00000  | sort -r -g -k2,2 -t$'\t' | head

Otherwise, spaces are used as delimiters.


### 1.3 Finding out about active substances directly

We go one step further. In the previous exercise, we did a word count on all columns in the original data. We now select one specific _column_.

Rewrite the mapper script to only send active substance names to the reducer. Call the resulting mapper script `mapper2.py`.

Mapper:

~~~python
#!/usr/bin/env python

# Lines are split on ',':
#  - good for CSV files
# Only 3d column is passed to reduce phase
#  - good for drugdb (AMM_det_H, active subst. column)


import sys

for line in sys.stdin:
    words = line.strip().split(",")
    print '%s\t%s' % (words[2], 1)
~~~

The reducer remains the same.

To run Hadoop:

~~~bash
hadoop jar /opt/hadoop/hadoop-tools/hadoop-streaming/target/hadoop-streaming-2.4.0.jar \
  -mapper mapper2.py \
  -reducer reducer.py \
  -input /mnt/bioinformatics_leuven/i0u19a/data/drugdb/AMM_det_H.csv \
  -output output
~~~

The most active substance? This is the top-10:

    cat  part-00000  | sort -r -g -k2,2 -t$'\t' | head



### 1.4 Active substances and maximum doses

Rewrite `mapper` and `reducer` such that not only do we count how many occurrences there are of a certain active substance, but also report the maximum dose.

*Important*: do this is 1 run.

Name the scripts `mapper3.py` and `reducer3.py`. Think of the assignments you did in preparation of this week's exercises.

Mapper:

~~~python
#!/usr/bin/env python

# Mapper for AMM_det_H.csv
# Lines are split on ',':
#  - good for CSV files
# 2 columns are passed to reducer:
#  - 3d column: Active Substance
#  - 5th column: Dose, double quotes are removed
# We pass 2 values (aka a list) to the reducer.
# Please note that key and value(s) are separated by '\t'

import sys

for line in sys.stdin:
    words = line.strip().split(",")
    print '%s\t%s,%s' % (words[2], 1, words[4].replace('"', ''))
~~~

Reducer:

~~~python
#!/usr/bin/env python

# A simple reducer, as used in the lecture
# This reducer can be used for:
#   - mapper3.py
# The two values are extracted and the maximum value
# of the dose is passed as an additional column in the output.


import sys

current_word = None
current_count = 0
max_dose = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, rest = line.split('\t')
    count, dose = rest.split(',')

    try:
        count = int(count)
    except ValueError:
        continue
    try:
        dose = float(dose)
    except ValueError:
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
        if max_dose < dose:
            max_dose = dose
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s\t%s' % (current_word, current_count, max_dose)
        current_count = count
        current_word = word
        max_dose = dose

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s\t%s' % (current_word, current_count, max_dose)
~~~

Hadoop run:

~~~bash
hadoop jar /opt/hadoop/hadoop-tools/hadoop-streaming/target/hadoop-streaming-2.4.0.jar \
  -mapper mapper3.py \
  -reducer reducer3.py \
  -input /mnt/bioinformatics_leuven/i0u19a/data/drugdb/AMM_det_H.csv \
  -output output
~~~

Is this a convenient way to work? What would make your life easier?

This is a poor way to pass additional data between two phases. We could use different approaches: `JSON`, ... Another option would be to use a datamodel and work with objects. These objects then need to be converted to a stream of data.


## 2. Normalization

### 2.1 Joins

Refer to the exercises on RDBMs, and look up what kind of questions we posed.

One of them was: _Which companies have compounds on the market with more than 10 active substances?_

Think of how you would approach that?


### 2.2 Normalization or not?

What is your opinion on normalization? Is it a good thing?


### 2.3 Reduce-side Join

Rewrite the map and reduce phase such that we can get the answer to the question above. Call the scripts `mapperJoin.py` and `reducerJoin.py`.

Mapper:

~~~
#!/usr/bin/env python

# Simple mapper, just like on the lecture slides
# Lines are split on spaces:
#  - good for word count
#  - not good for CSV or TSV files

import sys

abs_path = '/mnt/bioinformatics_leuven/i0u19a/data/drugdb/'

amm_det = open(abs_path + 'AMM_det_H.csv', 'r')
amm = open(abs_path + 'AMM_H.csv', 'r')

for line in amm:
    words = line.strip().split(',')
    print '%s.%s\t%s' % (words[1], "1", words[2])

for line in amm_det:
    words = line.strip().split(',')
    print '%s.%s\t%s' % (words[1], "2", words[2])
~~~

Reducer:

~~~
#!/usr/bin/env python

# This reduces the special-format output for joining
# The first entry (.1) is the compound
# The second entry and sometimes next ones are the substances

import sys

current_cti = None
current_name = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    keys, value = line.split('\t')
    cti,d = keys.split('.')

    if int(d) == 1:
        if current_cti:
            print '%s\t%s\t%s' % (current_cti, current_count, current_value)
        current_cti = cti
        current_count = 0
        current_value = value
    if int(d) == 2:
        current_count = current_count + 1

# do not forget to output the last word if needed!
print '%s\t%s\t%s' % (current_cti, current_count, value)
~~~

What is the top-10?

~~~bash
hadoop jar /opt/hadoop/hadoop-tools/hadoop-streaming/target/hadoop-streaming-2.4.0.jar \
  -mapper mapperJoin.py \
  -reducer reducerJoin.py \
  -input mapper.py \
  -output output
~~~

The `-input` flag is strange and is actually a dummy file as the real input files are defined in the mapper. Be careful, this would not work as-is on HDFS!

To get a sorted listing:

    cat  part-00000  | sort -r -g -k2,2 -t$'\t' | head

One more thing: ask yourself if this approach would work when running on a cluster. Why would this not be a good idea?


## 3. Spark

Do the same exercise as above with the drug database, but now using the Spark interactive shell. It can be launched in the following way:

~~~
pyspark
~~~

Refer to the examples given in the lecture and see how far you can get.

Take a look at: <http://spark.apache.org/docs/latest/programming-guide.html>

Some examples:


~~~python
file = sc.textFile("/mnt/bioinformatics_leuven/i0u19a/data/drugdb/AMM_det_H.csv")
counts = file.flatMap(lambda line: line.split(",")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
sorted = counts.map(lambda x: (x[1],x[0]) ).sortByKey(False)
~~~

Top-10

    sorted.take(10)

Paracetamol:

    sorted.filter(lambda x: x[1]=='"PARACETAMOL"').collect()

~~~
result2 = file.map(lambda line: line.split(",")) \
    .map(lambda x: x[2]) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)
result2.filter(lambda x: x[0] == '"PARACETAMOL"').collect()
~~~

Please remark the two types of quotes.

