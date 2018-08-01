# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:42:11 2018

@author: zhfliu
"""

# presents quantity

def myprint(sub):
    print(sub)
    sys.exit()  

def mycheck(Tlist):
    L = len(Tlist)
    Plist = [1] * L
    for i in range(L - 1):
        if Tlist[i] < Tlist[i + 1]:
             Plist[i + 1] = Plist[i] + 1
        elif Tlist[i] > Tlist[i + 1]:           
            if Plist[i] <= Plist[i+1]:
                Plist[i] = Plist[i+ 1] + 1            
    return sum(Plist)

def presentquatity(Mlist):   
    if Mlist == ['']:
        myprint(0)  
    if len(Mlist) == 1:
        myprint(1)
    tmp = mycheck(Mlist)
    Mlist.reverse()
    myprint(max(tmp, mycheck(Mlist)))

                
if __name__ == '__main__':
    import sys
    M = input().split(' ')
    presentquatity(M)

    
   
    