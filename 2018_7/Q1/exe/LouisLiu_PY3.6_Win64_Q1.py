# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:40:17 2018

@author: zhfliu
"""
# pick up the surplus sand.

def mycomp(sand1, sand2):
   
    for k in sand1:
        D_s[k] = D_s.get(k, 0) + 1
    for k in sand2:
        D_t[k] = D_t.get(k, 0) + 1
        
    if len(D_s.keys()) != len(D_t.keys()):
        for k in D_t.keys():
            if k not in D_s.keys():
                print(k)
                break
    else:
        for k in D_s.keys():
            if D_s[k] == D_t[k]:
                continue
            else:
                print(k)
                break

if __name__ == '__main__':

    s = input()
    t = input()
    
    D_s = {}
    D_t = {}
    
    mycomp(s, t)
    