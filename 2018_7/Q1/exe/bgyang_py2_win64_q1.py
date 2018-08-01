#!/usr/bin/python

s=raw_input().strip(" ")
t=raw_input().strip(" ")

s1=sorted(s)
t1=sorted(t)

n=min(len(s1), len(t1))

if len(s1)>len(t1):
    for i in range(0,n):
        if s1[i]!=t1[i]:
            print s1[i]
            break
    else:
        print s1[len(s1)-1]
				
if len(s1)<len(t1):
    for i in range(0,n):
        if s1[i]!=t1[i]:
            print t1[i]
            break
    else:
        print t1[len(t1)-1]

##for i in range(0,n):
##    if s1[i]!=t1[i] and len(s1)<len(t1):
##        print t1[i]
##        break
##        
##    if s1[i]!=t1[i] and len(s1)>len(t1):
##        print s1[i]
##        break
##

        
##    if s1 in t1:
##        print t1[len(t1)-1]  

##for i in range(0,n):   
##    if s1[i]==t1[i] and len(s1)>len(t1):
##        continue
##    print s1[len(s1)-1]
##
##    if s1[i]==t1[i] and len(s1)<len(t1):
##        pass
##    print t1[len(t1)-1]

##s2=set(s1)
##t2=set(t1)
##print s2
##print t2

##s2=list(set(s1))
##t2=list(set(t1))
####print s2
####print t2
##
##
##s3=set(s2)
##t3=set(t2)
##print s3
##print t3

##c=t1.symmetric_difference(s1)
####print c
##for ele in c:
##    print ele
