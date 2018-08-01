#coding=utf8
import sys,os
reload(sys)
sys.setdefaultencoding( "utf-8" )

def countchar(strs,strt):
	str1=strs.lower() #化成小写
	str2=strt.lower()
	sc1=set(str1)
	sc2=set(str2)
	if sc2>sc1:
		datares=[]
		[datares.append(i) for i in sc2 if not i in sc1]
		return datares[0]
	else:
		for i1 in sc1:
			if str1.count(i1) != str2.count(i1):
				return i1
if __name__ == "__main__":
	strs = raw_input()
	strt = raw_input()
	print(countchar(strs,strt))