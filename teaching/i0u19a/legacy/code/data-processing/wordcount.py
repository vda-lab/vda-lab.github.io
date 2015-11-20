#!/usr/bin/python

import sys

wordcount={}

for line in sys.stdin:
  line = line.strip()
  for word in line.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
  print k, v

