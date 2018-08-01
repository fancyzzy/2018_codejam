#coding=utf8
import sys,os
reload(sys)
sys.setdefaultencoding( "utf-8" )

def AddItem(ind):
	y=scores[ind-1]
	x=scores[ind]
	#print ind,x,y,gift[ind],gift[ind-1]
	if x>y :
		gift[ind]=gift[ind-1]+1
	else:
		if x==y:
			gift[ind]=1
		else:
			gift[ind]=1
			if gift[ind-1]<=gift[ind]:
				ii=ind
				while ii>1 :
					ii-=1
					m=scores[ii-1]
					n=scores[ii]
					gift[ii]=gift[ii+1]+1	
					#print gift
					if ((n >= m) or ( (gift[ii] < gift[ii-1]) and (n<m) ))  :
						break;					
					
scores=[]
gift=[]
if __name__ == "__main__":
	line1=raw_input().split(' ')
	scores=[0]
	[scores.append(int(i)) for i in line1]
	scores[0]=scores[1]
	
	
	gift=[1]*(len(line1)+2)	
	
	for i in range(1,len(line1)+1):
		AddItem(i)
	#	if line2[i]>line2[i-1]:
	#		gift[i]=max(gift[i],gift[i-1])+1
	#		print gift
	#gift[0]=0
	#gift[len(line1)+1]=0
	#print gift
	gift[0]=0
	gift[len(line1)+1]=0
	print sum([i for i in gift])