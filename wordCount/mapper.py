#!/usr/bin/python

import sys
import re

for line in sys.stdin:
	line = line.split('\t')
	regex0 = '|'.join(re.split('\W+',line[4]))
	node, body = line[0], regex0
	print '{0}\t{1}'.format(node,body)
