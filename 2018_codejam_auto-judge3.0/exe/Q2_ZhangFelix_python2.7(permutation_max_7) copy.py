#!/usr/bin/env python
#__*__coding:utf-8__*__

import itertools
import time

def time_me(fn):
    def _wrapper(*args, **kwargs):
        start = time.clock()
        fn(*args, **kwargs)
        print('%s cost %.3f second' % (fn.__name__, time.clock() - start))
    return _wrapper

@time_me
def find(l,n):
	global d
	max_com = []
	m_value = 0
	all_re = []
	ll = [x for x in range(1,n+1)]

	print "ll = ",ll
	#不需要那么多循环
	nn = 0	
	for m in l:
		nn += 1
		if nn >= n:
			break
		lv = ll[:]
		lv.remove(m[1])
		lv.remove(m[2])
		#至少4个数才能进行下一个循环
		if n <= 3:
			sum_v = m[0]
			if m_value < sum_v:
				m_value = sum_v
				max_com.append(m)
			break
		print "m = ",m
		print "lv = ",lv	
		lp = list(itertools.permutations(lv))

		lpp = lp[:]
		#处理掉重复的项目
		print "DEBUG len(lp) = ",len(lp)
		for item in lpp:
			for i in range(0,len(item)-1,2):
				if item[i]>item[i+1]:
					lp.remove(item)
					break

		print "DEBUG after filtering, len(lp) = ",len(lp)

		for item in lp:
			re = []
			re.append(m)
			print "DEBUG item:",item
			for i in range(0,len(item)-1,2):
				#print "DEBUG:({0},{1})".format(item[i-2],item[i-1])
				v = d[(item[i],item[i+1])]
				re.append((v,item[i],item[i+1]))
				if len(re) == n/2:
					print "Debug re = ",re
					sum_v = 0
					for x in re:
						sum_v += x[0]
					if m_value < sum_v:
						m_value = sum_v
						max_com = re[:]
					break
				else:
					continue

	print "max_com = ",max_com
	print "The max value = ",sum(zip(*max_com)[0])
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

	d = {}
	for item in lvalue:
		d[(item[1],item[2])] = item[0]
	print "dictionary d= ",d


	print "lvalue=",lvalue


	result = find(lvalue,n)
	print "result = ",result	