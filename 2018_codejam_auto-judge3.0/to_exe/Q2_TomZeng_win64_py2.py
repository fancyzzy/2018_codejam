#!/usr/bin/python
# -*- coding: UTF-8 -*-
total_num = int(raw_input());
matrix = [[0 for i in range(total_num)] for i in range(total_num)];
for i in range(0,total_num):
	matrix[i] = raw_input().split();

box = range(total_num);
resultList = [];
def getPair(box, result):
	if(len(box)<=1):
		resultList.append(result);
	else:
		p1 = box[0];
		if(len(box)%2==0):
			box1 = range(1,len(box));
		else:
			box1 = range(0,len(box));
		for k in box1:
			p2 = box[k];
			box2 = box[:];
			box2.remove(p1);
			if(p1!=p2):
				box2.remove(p2);
			result2 = result + int(matrix[p1][p2]);
			getPair(box2, result2);
getPair(box,0);
print max(resultList);

