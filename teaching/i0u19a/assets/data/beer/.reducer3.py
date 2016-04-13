#!/usr/bin/env python
import sys

previous_percentage = ''
all_beers = []
all_breweries = []

for line in sys.stdin:
	line = line.strip()
	key, value = line.split("\t")
	beer, brewery = value.split(",")
	percentage = key
	if percentage != previous_percentage:
		if previous_percentage != '':
			all_beers = list(set(all_beers))
			all_breweries = list(set(all_breweries))
			print previous_percentage, "\t", float(len(all_beers))/len(all_breweries), "\t", len(all_beers), "\t", all_beers, "\t", len(all_breweries), "\t", all_breweries
		all_beers = [beer]
		all_breweries = [brewery]
		previous_percentage = percentage
	else:
		all_beers.append(beer)
		all_breweries.append(brewery)


all_beers = list(set(all_beers))
all_breweries = list(set(all_breweries))
print previous_percentage, "\t", float(len(all_beers))/len(all_breweries), "\t", len(all_beers), "\t", all_beers, "\t", len(all_breweries), "\t", all_breweries
