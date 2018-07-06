#!/usr/bin/env python
#--*--coding:utf-8--*--

import copy

def del_x(l,x):
	#减去去l列表中和x元素有任意相同坐标的元素
	ll = copy.deepcopy(l) 
	for item in l:
		f = False
		#第一个元素是value不是坐标
		for i in range(1,len(item)):
			for j in range(1,len(x)):
				if item[i] == x[j]:
					ll.remove(item)
					f = True
					break
			if f:
				break
	return ll


def input_l():
	n = input()
	#l_all = [(value,i,i+1),(value2,i,i+2)...(value(n(n-1)/2),i+n-2,i+n-1)]
	l_all = []
	l = []
	for i in range (1,n+1):
		l = raw_input().split()
		for j in range(i+1,n+1):		
			l_all.append((int(l[j-1]),i,j))

	l_all = sorted(l_all, reverse=True)
	return n,l_all


def find_re(l_all,n):

	if len(l_all) == 0:
		return 0
	if len(l_all) == 1 or n == 1:
		return l_all[0][0]

	ll = []
	new_all = []
	l_copy = l_all[:]

	for i in range(len(l_all)/2):
		l_copy.remove(l_all[i])	
		new_all = del_x(l_copy,l_all[i])
		ll.append(l_all[i][0] + find_re(new_all[:], n-1))

	return max(ll[:])

			
################find_re()#####################

if __name__ == '__main__':

	n,l_all = input_l()
	res = find_re(l_all,n/2)	
	print res
