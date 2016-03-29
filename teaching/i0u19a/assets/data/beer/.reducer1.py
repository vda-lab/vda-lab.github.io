#!/usr/bin/env python
import sys

previous_value = ''
sum = 0

for line in sys.stdin:
	line = line.strip()
	value, count = line.split("\t")
	count = int(count)
	if value != previous_value:
		if previous_value != '':
			print previous_value, "\t", sum
		sum = 1
		previous_value = value
	else:
		sum += 1

print previous_value, "\t", sum
