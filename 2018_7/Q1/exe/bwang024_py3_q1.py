#!/usr/bin/env python
# -*- coding: UTF-8 -*-
firstInput=list(input())
secondInput=list(input())
firstInput.sort()
secondInput.sort()
for i in range(len(secondInput)):
    if firstInput[i]==secondInput[i]:
        i+=1
    else:
        print(secondInput[i])
        break

