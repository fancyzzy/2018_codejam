#!/usr/bin/env python
import os
import sys


def getsand():

	s = raw_input()


	s = sorted(s)

	t = raw_input()

	t = sorted(t)
	l = len(s)
	m = len(t)
	if (l > 1000) or (m > 1000):
		print "input too long"
		quit()

	n = 0

	while l > 0:
		if s[n] == t[n]:
			n = n + 1
			l = l - 1
		else:
			print t[n]
			break

	if l == 0:
		print t[-1]	
	
	
if __name__ == '__main__':
	getsand()