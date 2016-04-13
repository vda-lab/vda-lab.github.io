#!/usr/bin/env python
import sys

previous_percentage = ''
all_names = []

for line in sys.stdin:
	line = line.strip()
	percentage, name = line.split("\t")
	if percentage != previous_percentage:
		if previous_percentage != '':
			print previous_percentage, "\t", len(all_names), "\t", all_names
		all_names = [name]
		previous_percentage = percentage
	else:
		all_names.append(name)

print previous_percentage, "\t", len(all_names), "\t", all_names.append
