#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from operator import itemgetter
a=raw_input()#input the line num 
n=int(a)

data=[]
new_data=[]
up_data=[]
final=[]
for i in range(n):
    x=raw_input()
    data.append(x)

for i in range(n):

    data[i]=[int(n) for n in data[i].split()]

    if data[i][1]<data[i][2]:
        data[i][1],data[i][2]=data[i][2],data[i][1]

for idata in data:
    if idata not in new_data:
        new_data.append(idata)

up_data=sorted(new_data,key=itemgetter(0,1,2))  

for i in range(0,len(up_data)):
    for each in range(3):
        print up_data[i][each],
    print "\r"

