
# Data Processing Exercises

## Word count and beyond

###  Word count using Hadoop Streaming

Implement the Python `mapper` and `reducer` scripts on the slides of week 6. Run the Hadoop streaming API on the Amazon server. Use the '' dataset for this.

Does this work? Does it give some insight? Why (not)?

What about splitting the lines (in the mapper) on ',' instead of spaces? Adapt the `mapper.py` script.

Does this work? Does it give some insight? Why (not)?

How many times is PARACETAMOL the active substance?

What is the most used substance?

Please note that in order to effectively sort in a tab-delimited dataset, you need to the following:

    cat  part-00000  | sort -r -g -k2,2 -t$'\t' | head


### Finding out about active substances directly

We go one step further. In the previous exercise, we did a word count on all columns in the original data.

Rewrite the mapper script to only send active substance names to the reducer.


### Active substances and maximum doses

Rewrite `mapper` and `reducer` such that not only do we count how many occurrences there are of a certain active substance, but also report the maximum dose.

*Important*: do this is 1 run.

Think of the assignments you did in preparation of this week's exercises.

Is this a convenient way to work? What would make your life easier?
 

## Normalization

### Joins

Refer to the exercises on RDBMs, and look up what kind of questions we posed.

One of them was: _Which companies have compounds on the market with more than 10 active substances?_

Think of how you would approach that?


### Normalization or not?

What is your opinion on normalization? Is it a good thing?


## Spark

Do the same exercise as above with the drug database, but now using the Spark interactive shell. It can be launched in the following way:

```
/mnt/bioinformatics_leuven/incubator-spark/bin/pyspark
```

Refer to the examples given in the lecture and see how far you can get.


