#!/usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()
	fields = line.split(',')
	print fields[3], "\t", fields[1], ',', fields[4]
