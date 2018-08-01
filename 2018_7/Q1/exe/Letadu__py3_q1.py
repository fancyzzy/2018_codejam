#!/usr/bin/python

A_str = input ()
##print (A_str)

B_str = input ()
##print(B_str)
C = 0
D = 0
for i in [chr(x) for x in range( 97,123)]:
    C= A_str.count(i)
    D= B_str.count(i)
    if C != D:  
         print(i)
         

    
