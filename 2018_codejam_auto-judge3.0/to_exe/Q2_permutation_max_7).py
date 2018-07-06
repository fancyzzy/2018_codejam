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
	lvalue = [(99, 4, 7), (95, 2, 10), (93, 1, 8), (91, 4, 5), (90, 2, 11), (85, 6, 10), (85, 3, 9), (82, 3, 6), (80, 1, 11), (76, 4, 8), (76, 1, 10), (75, 6, 9), (69, 1, 3), (68, 6, 8), (67, 8, 10), (66, 8, 11), (66, 1, 7), (65, 4, 6), (64, 2, 8), (61, 7, 10), (58, 4, 9), (56, 3, 5), (54, 2, 7), (52, 5, 6), (49, 7, 8), (43, 5, 8), (42, 9, 10), (40, 5, 10), (40, 2, 6), (35, 2, 4), (35, 1, 4), (34, 9, 11), (31, 2, 9), (30, 6, 11), (29, 1, 2), (28, 5, 9), (22, 6, 7), (21, 10, 11), (20, 3, 11), (19, 5, 11), (19, 3, 10), (19, 2, 5), (18, 1, 6), (17, 1, 5), (15, 4, 11), (15, 3, 7), (15, 2, 3), (13, 4, 10), (11, 7, 11), (10, 8, 9), (9, 7, 9), (9, 5, 7), (7, 3, 4), (4, 3, 8), (3, 1, 9)]

	n = 11	

	d = {}
	for item in lvalue:
		d[(item[1],item[2])] = item[0]
	print "dictionary d= ",d


	print "lvalue=",lvalue


	result = find(lvalue,n)
	print "result = ",result	