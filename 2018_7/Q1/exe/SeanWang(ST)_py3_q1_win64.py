# GSM CodeJam, July 2018
#!/usr/bin/env python3.5


str1 = input()
str2 = input()
list1 = list(str1)
list2 = list(str2)

list1.sort()
list2.sort()

l2 = len(list2)


for i in range(l2):
       if list1[i] != list2[i]:
        print(list2[i])
        break
