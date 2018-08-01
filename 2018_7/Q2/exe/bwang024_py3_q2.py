#!/usr/bin/env python
# -*- coding: UTF-8 -*-
memberScore=list(input())
#memberScore=raw_input()
prizeNum1=[0 for i in range(len(memberScore))]
prizeNum2=[0 for i in range(len(memberScore))]
for i in range(memberScore.count(" ")):
    memberScore.remove(" ")
#print(memberScore)

#找到分数最低的，奖品为1，记下minIndex
minScore =min(memberScore)
minIndex=memberScore.index(minScore)
#print(minIndex)

#该分数最低的跟下一个比较分数大小
prizeNum1[minIndex]=1
if minIndex<len(memberScore)-1:
    for i in range(minIndex,len(memberScore)-1):
        if memberScore[i] < memberScore[i+1]:
            prizeNum1[i+1] = prizeNum1[i]+1

            #print(prizeNum1[i+1])

            if minIndex<len(memberScore)-2:
                if memberScore[i+2]<=memberScore[i+1]:
                    prizeNum1[i+2] = prizeNum1[i+1] - 1
                else:
                    prizeNum1[i+2] = prizeNum1[i+1] + 1
        else:
            prizeNum1[i+1] = prizeNum1[i] - 1
    i += 1
#print(prizeNum1)
#如果下个分数大，奖品+1，若相等，奖品为1
#到最下面之后，再往上比较
memberScore.reverse()
minIndex=memberScore.index(minScore)
prizeNum2[minIndex]=1
if minIndex<len(memberScore)-1:
    for i in range(minIndex,len(memberScore)-1):
        if memberScore[i] < memberScore[i+1]:
            prizeNum2[i+1] = prizeNum2[i]+1
            if minIndex<len(memberScore)-2:
                if memberScore[i+2]<=memberScore[i+1]:
                    prizeNum2[i+2] = prizeNum2[i+1] - 1
                else:
                    prizeNum2[i+2] = prizeNum2[i+1] + 1
        else:
            prizeNum2[i+1] = prizeNum2[i] - 1
    i += 1
#prizeNumSum=sum(prizeNum)
#print(prizeNum2)
prizeSum=sum(prizeNum1)+sum(prizeNum2)-1
print(prizeSum)