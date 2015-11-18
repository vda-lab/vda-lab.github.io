#!/usr/bin/env python

# Simple mapper, just like on the lecture slides
# Lines are split on spaces:
#  - good for word count
#  - not good for CSV or TSV files

import sys

amm_det = open('../../data/drugdb/AMM_det_H.csv', 'r')
amm = open('../../data/drugdb/AMM_H.csv', 'r')

for line in amm:
	words = line.strip().split(',')
	print '%s.%s\t%s' % (words[1], "1", words[2])	

for line in amm_det:
	words = line.strip().split(',')
	print '%s.%s\t%s' % (words[1], "2", words[2])	
