#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.split()
	if len(data) == 10:
		h,l,u,t,ts,rGET,r,rHTTP,s,b = data
		r = r.replace('http://www.the-associates.co.uk','')
		print '{0}\t{1}'.format(r,1)
