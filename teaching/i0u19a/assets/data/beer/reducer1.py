#!/usr/bin/env python
import sys

previous_value = ''
sum = 0

for line in sys.stdin:
	line = line.strip()
	value, count = line.split("\t")
	count = int(count) # The count is read as a string, but needs to be converted into an integer.
	if value != previous_value:
		# What needs to be done if a new value is encountered?
		WRITE_CODE_HERE
	else:
		sum += 1

print previous_value, "\t", sum
