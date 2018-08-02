#!/usr/bin/env python
# -*- coding: UTF-8 -*-
shazi1 = list(input())
shazi2 = list(input())
shazi2.sort()
shazi1.sort()
target = len(shazi2)-1
for j in range(target):
    if shazi1[j] != shazi2[j]:
        target = j
        break

print(shazi2[target])

if __name__ == '__main__':
    pass