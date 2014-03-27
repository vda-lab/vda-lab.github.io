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

