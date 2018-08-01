#!/usr/bin/Python

List1 = list(raw_input())
List2 = list(raw_input())

i=0
while i < len(List1):
    for temp in List1:
        if temp in List2:
            List1.remove(temp)
            List2.remove(temp)
        else:
            break
i+=1

print List2[0]
