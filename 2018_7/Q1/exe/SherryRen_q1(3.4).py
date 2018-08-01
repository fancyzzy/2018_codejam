#!/usr/bin/env python
# -*- coding: UTF-8 -*-
shazi1 = list(input())
shazi2 = list(input())
shazi1.sort()
shazi2.sort()
target = len(shazi2)-1
for i in range(target):
    if shazi1[i] != shazi2[i]:
        target = i
        break

print(shazi2[target])