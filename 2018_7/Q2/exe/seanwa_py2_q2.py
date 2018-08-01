#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'seanwa'

# main function
R = 0
Flag = False
M = raw_input()
if len(M) == 0:
	print 0
	exit(0)
elif len(M) == 1:
	print 2
	exit(0)

M = list(M.split(" "))
if len(M) == 2:
	if M[0] != M[1]:
		 print 3
	else:
		print 2
else:
	for i in range(1, len(M) - 1):
		if M[i] > M[i-1] or M[i] > M[i+1]:
			if Flag:
				R += 2
			else:
				R += 1
			Flag = True
		else:
			Flag = False
	if M[0] > M[1]:
		R += 1
	if M[-1] > M[-2]:
		R += 1
	print (R + len(M))