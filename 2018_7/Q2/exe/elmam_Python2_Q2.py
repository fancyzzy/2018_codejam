#!/usr/bin/Python

str = raw_input()
array = str.split(" ")

#init
Num=[None]*len(array)

TotalNum=0

#each one has 1 gift
i=0
while i < len(array):
    Num[i]="1"
    i+=1

# true:Num[] has changed, need to loop again,false for no change    
flag = False

#compare the neighbors' score and mark the bigger score's gift=lower's +1
j=0
if len(array)>1:
    while j < len(array)-1:
        flag = False
        if array[j] > array[j+1]and int(Num[j])<=int(Num[j+1]):
            Num[j]=int(Num[j+1])+1
            flag = True
            
        if array[j] < array[j+1] and int(Num[j])>=int(Num[j+1]):
            Num[j+1]=int(Num[j])+1
            flag = True
            
        if flag == True:
            j=0
        else:
            j+=1
            
#calculate the total number of gift
k=0    
while k < len(Num):
    TotalNum+=int(Num[k])
    k+=1

print TotalNum
