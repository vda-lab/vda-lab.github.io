#!/usr/bin/env python

# Mapper for AMM_det_H.csv
# Lines are split on ',':
#  - good for CSV files
# 2 columns are passed to reducer:
#  - 2nd column: Active Substance
#  - 5th column: Dose, double quotes are removed
# We pass 2 values (aka a list) to the reducer.
# Please note that key and value(s) are separated by '\t'

import sys

for line in sys.stdin:
    words = line.strip().split(",")
    print '%s\t%s,%s' % (words[2], 1, words[4].replace('"', ''))

