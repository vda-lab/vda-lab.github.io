#!/usr/bin/env python

# A simple reducer, as used in the lecture
# This reducer can be used for:
#   - mapper3.py
# The two values are extracted and the maximum value
# of the dose is passed as an additional column in the output.


import sys

current_word = None
current_count = 0
max_dose = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, rest = line.split('\t')
    count, dose = rest.split(',')

    try:
        count = int(count)
    except ValueError:
        continue
    try:
        dose = float(dose)
    except ValueError:
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
        if max_dose < dose:
            max_dose = dose
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s\t%s' % (current_word, current_count, dose)
        current_count = count
        current_word = word
        max_dose = dose

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s\t%s' % (current_word, current_count,dose)
