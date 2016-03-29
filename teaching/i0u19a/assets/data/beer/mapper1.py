#!/usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()
	fields = line.split(',')
	
	# Print the third field and a 1, separated by a tab.
	ALTER_THIS_LINE
