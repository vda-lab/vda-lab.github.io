#!/usr/bin/env python

# This reduces the special-format output for joining
# The first entry (.1) is the compound
# The second entry and sometimes next ones are the substances

import sys

current_cti = None
current_name = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    keys, value = line.split('\t')
    cti,d = keys.split('.')

#    print cti, d

    if int(d) == 1:
        if current_cti:
            print '%s\t%s\t%s' % (current_cti, current_count, current_value)
        current_cti = cti
        current_count = 0
        current_value = value
    if int(d) == 2:
        current_count = current_count + 1

# do not forget to output the last word if needed!
print '%s\t%s\t%s' % (current_cti, current_count, value)