#!/usr/bin/python
# -*- coding: UTF-8 -*-


def gift(mlist):
    num = len(mlist)
    res = [1] * num
    for i in range(0, num - 1):
        if mlist[i + 1] > mlist[i]:
            res[i + 1] = res[i] + 1
    for j in range(num - 1, 0, -1):
        if mlist[j - 1] > mlist[j] and res[j - 1] <= res[j]:
            res[j - 1] = res[j] + 1
    return sum(res)


if __name__ == '__main__':
    score = str(raw_input())
    m_list = [int(item) for item in score.split()]
    print gift(m_list)

