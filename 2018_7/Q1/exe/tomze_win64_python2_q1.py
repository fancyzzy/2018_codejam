#!/usr/bin/python
# -*- coding: UTF-8 -*-


def checklist(list1, list2):
    while True:
        item = list1.pop()
        try:
            list2.remove(item)
        except:
            return item


if __name__ == '__main__':
    s = str(raw_input())
    t = str(raw_input())
    s_list = list(s)
    t_list = list(t)
    print checklist(t_list, s_list)
