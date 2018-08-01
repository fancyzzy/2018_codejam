#!/usr/bin/python

a = [] 
str = raw_input()
pingfen = str.split(" ")
##print pingfen

n=len(pingfen)
##print n

jiangpin=[1 for i in range(0,n)]
##print jiangpin

for i in range(0,n-1):
    if pingfen[i]>pingfen[i+1]:
        jiangpin[i]+=1
for i in range(n-1,0,-1):
    if pingfen[i]>pingfen[i-1]:
        jiangpin[i]+=1
    
s=0
for ele in jiangpin:
    s+=ele
print s


