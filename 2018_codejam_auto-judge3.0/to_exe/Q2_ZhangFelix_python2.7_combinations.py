#!/usr/bin/env python
#__*__coding:utf-8__*__

import itertools
import time

def time_me(fn):
    def _wrapper(*args, **kwargs):
        start = time.clock()
        re = fn(*args, **kwargs)
        print('%s cost %.3f second' % (fn.__name__, time.clock() - start))
       	return re 
    return _wrapper

#@time_me
def find(l,n):
	ll = list(itertools.combinations(l,n/2))
	
	max_sum = 0
	max_com = []
	for item in ll:
		ids = []
		f = False
		for i in range(len(item)):
			if (item[i][1] in ids) or (item[i][2] in ids):
				f = True	
				break
			else:
				ids.append(item[i][1])
				ids.append(item[i][2])

		if f:
			continue
		each_sum = sum(zip(*item)[0])
		if max_sum < each_sum:
			max_sum = each_sum
			max_com = []
			max_com.append(item)
		elif max_sum == each_sum:
			max_com.append(item)

	return max_com


if __name__ == "__main__":

	#Input
	n = input()
	lvalue = []
	for i in range(1,n+1):
		l = raw_input().split()			
		for j in range(i+1,n+1):
			lvalue.append((int(l[j-1]),i,j))

	lvalue = sorted(lvalue,reverse=True)
	print "DEBUG lvalue = ",lvalue

	d = {}
	for item in lvalue:
		d[(item[1],item[2])] = item[0]

	max_re = []	
	max_re = find(lvalue,n)

#	print "result:",max_re
	print sum(zip(*max_re[0])[0])
