#!/usr/bin/python

S = input()
P_score= S.split(" ")


#print (S)
for i in range (0,len(P_score)):
    if P_score[i] != ' ':
        P_score[i]= int(P_score[i])
    
List_J=[1 for m in range(0,len(P_score))]## set default List_J as "1"   
for i in range(0,(len(P_score)-1)):
    if P_score[i] < P_score[i+1]:
        List_J[i+1] = List_J[i]+1
        i += 1    
    elif P_score[i]>P_score[i+1]:
        if List_J[i]== List_J[i+1]:
                
            List_J[i]+=1    
            k=i-1
            q=i
            while i<len(P_score)-1:
                if P_score[k]<=P_score[q]:
                    i +=1
                    break
                if P_score[k]>P_score[q]:
                    if List_J[k]>List_J[q]: break
                    if List_J[k]==List_J[q]:
                        List_J[k]+= 1            
                k -= 1
                q -= 1
        i += 1
print(sum(List_J))

