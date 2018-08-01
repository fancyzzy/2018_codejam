#!/usr/bin/env python
# -*- coding: UTF-8 -*-
score=input().split()
score_ori=score[:]##before sort
score.sort()##after sort
num=len(score)
index_s=[0 for i in range(num)]
num_gift=[0 for i in range(num)]
flag_index=[0 for i in range(num)]
sum=0
for i in range(0,num):
	for j in range(0,num):
		if score[i]==score_ori[j] and flag_index[j]==0:
			flag_index[j]=1
			index_s[i]=j
			break
num_gift[index_s[0]]=1
for i in range(1,num):
	if index_s[i]==num-1:
		if score_ori[num-1]!=score_ori[num-2]:
			num_gift[num-1]=num_gift[num-2]+1
		else:
			num_gift[num-1]=1
	elif index_s[i]==0:
		if score_ori[0]!=score_ori[1]:
			num_gift[0]=num_gift[1]+1
	else:
		if num_gift[index_s[i]-1]>num_gift[index_s[i]+1]:
			if score_ori[index_s[i]-1]==score_ori[index_s[i]]:
				max=0
			else:
				max=num_gift[index_s[i]-1]
		elif num_gift[index_s[i]-1]==num_gift[index_s[i]+1]:###
			if score_ori[index_s[i]-1]==score_ori[index_s[i]+1]:
				max=0
			elif score_ori[index_s[i]-1]>score_ori[index_s[i]+1]:
				max=num_gift[index_s[i]+1]
			else:
				max=num_gift[index_s[i]-1]
		else:
			if score_ori[index_s[i]]==score_ori[index_s[i]+1]:
				max=0
			else:
				max=num_gift[index_s[i]+1]
		num_gift[index_s[i]]=max+1
for nu in num_gift:
	sum=sum+int(nu)
print(sum)






