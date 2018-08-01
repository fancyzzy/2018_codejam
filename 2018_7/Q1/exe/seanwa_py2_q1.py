#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'seanwa'

# main function
s = list(raw_input())
s.sort()
t = list(raw_input())
t.sort()
r = 0
for i in range(len(s)):
	if s[i] != t[i]:
		r = t[i]
		break
	
if r == 0:
	print t[-1]
else:
	print r
