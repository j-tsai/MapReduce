#!/usr/bin/python

import sys


fantastic = 0
fantastically = []
for line in sys.stdin:
    data = line.split("\t")
    if len(data) != 2:
        continue

    node = data[0]
    body = data[1].split('|')
    fantastic += body.count('fantastic')
    if 'fantastically' in body:
        fantastically.append(int(node))
print "num 'fantastic':", "\t", fantastic
print "list of csv nodes the word 'fantastically' found:", "\t", ','.join(map(str,sorted(fantastically)))
