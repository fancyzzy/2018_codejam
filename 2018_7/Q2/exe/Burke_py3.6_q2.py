#!/usr/bin/python
# _*_ coding: utf-8 _*_

scoreL = input().split()
actorN = len(scoreL)
prizeL = [1] * actorN
global reverseN
reverseN = 0

for i in range(1,actorN-1):
    if int(scoreL[i-1])>int(scoreL[i]):      
        if int(scoreL[i])>int(scoreL[i+1]):
            reverseN +=1
        
        else:  
            if prizeL[i-reverseN-1] < reverseN + 2: prizeL[i-reverseN-1] = reverseN +2
                                    
            for j in range(1,reverseN +1):
                prizeL[i-j] +=j
            reverseN = 0
            
        if i == actorN-2 and int(scoreL[i])>int(scoreL[i+1]): 
            for j in range(reverseN):
                prizeL[i-j] =prizeL[i-j+1]+1
                
            prizeL[i-reverseN] = max(prizeL[i-reverseN], prizeL[i+1] + 1 + reverseN)
                
    elif int(scoreL[i-1]) < int(scoreL[i]): prizeL[i] = prizeL[i-1] + 1
        
    elif int(scoreL[i-1]) == int(scoreL[i]):
        if int(scoreL[i])<= int(scoreL[i+1]): prizeL[i] = 1
        else:
            prizeL[i] = 2

if int(scoreL[actorN-2]) < int(scoreL[actorN-1]): prizeL[actorN-1] = prizeL[actorN-2] + 1

#print('scoreL= ',scoreL)
#print('prizeL= ',prizeL)
print(sum(prizeL))
