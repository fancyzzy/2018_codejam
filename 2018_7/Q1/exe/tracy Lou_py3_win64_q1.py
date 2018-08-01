#!/usr/bin/env python
# -*- coding: UTF-8 -*-
s=list(input())
s.sort()
t=list(input())
t.sort()
flag=0
num=len(s)
for i in range(0,num):
	if s[i]!=t[i]:
		print(t[i])
		flag=1
		break
if flag==0:
	print(t[num])


