#!/usr/bin/python

import sys

current_word = None
current_count = 0
word = None
maxWord = None
maxCount = 0

for line in sys.stdin:
	word, count = line.split("\t",1)
	try:
		count = int(count)
	except ValueError:
		continue
	if current_word == word:
		current_count += count
	else:
# print counts of each path 
#		if current_word:
#			print '%s\t%s' % (current_word, current_count)
		if current_count > maxCount:
			maxCount = current_count
			maxWord = current_word
		elif current_count == maxCount:
			maxWord += '\n' + current_word
		current_count = count
		current_word = word

# print last line if necessary
#if current_word == word:
#	print '%s\t%s' % (current_word, current_count)
print '%s\t%s' % (maxCount, maxWord)		
