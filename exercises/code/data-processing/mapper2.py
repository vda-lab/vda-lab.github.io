#!/usr/bin/env python

# Lines are split on ',':
#  - good for CSV files
# Only 2nd column is passed to reduce phase
#  - good for drugdb (AMM_det_H, active subst. column)


import sys

for line in sys.stdin:
    words = line.strip().split(",")
    print '%s\t%s' % (words[2], 1)

