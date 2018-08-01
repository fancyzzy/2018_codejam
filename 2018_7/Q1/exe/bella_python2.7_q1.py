#!/usr/bin/python
# -*- coding: UTF-8 -*-

cmd1 = raw_input().strip(" ");
cmd2 = raw_input().strip(" ");
a = list(cmd1)
b = list(cmd2)
a.sort()
b.sort()
ret1 = list(set(a))
ret2 = list(set(b))
ret1.sort(key = a.index)
ret2.sort(key = b.index)
m1 = []
m2 = []
	
diff = list(set(a) ^ set(b))

if diff :
	print diff[0]
else :
	
	for item in ret1:
		#print("the %s has found %d" %(item, a.count(item)))
		m1.append(a.count(item))
	for item in ret2:
		#print("the %s has found %d" %(item, b.count(item)))
		m2.append(b.count(item))
	
	for i in range(len(m2)):
		if m1[i] != m2[i] :
			#print m2[i]
			print ret2[i]
			break
	
	
	
	



