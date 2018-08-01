#!/usr/bin/python
# -*- coding: UTF-8 -*-
b=raw_input()# stand for t
a=raw_input()# stand for s

list_a=[]
i=0
for sub in a:
    x=a.count(sub,0,len(a))
    y=b.count(sub,0,len(b))
    #print sub, a.count(sub,0,len(a)),b.count(sub,0,len(b))
    if (x!=y):
        print sub
        break


   



