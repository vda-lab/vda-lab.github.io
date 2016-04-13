#!/usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()
	fields = line.split(',')

	# Print the third field followed by a tab, and then the beer name and
	# brewery name, separated by a comma.
	# Like this:
	# 6.5    V Cense,Brasserie de Jandrain-Jandrenouille
	# 8      Aardmonnik,De Struise Brouwers
	ALTER_THIS_LINE
