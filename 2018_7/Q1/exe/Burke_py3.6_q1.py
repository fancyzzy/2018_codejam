#!/usr/bin/python
# _*_ coding: utf-8 _*_

s = sorted(list(input()))
t = sorted(list(input()))

tt = t[:]
n = len(s)
i = 0
findR = False
while i<n:
    if s.pop() != tt.pop():
        print(t[n-i])
        findR = True
        break
    i += 1
if len(s) == 0 and findR == False:
    print(tt[0])
