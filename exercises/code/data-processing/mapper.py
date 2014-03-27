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

