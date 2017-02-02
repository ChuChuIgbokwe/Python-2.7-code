#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 20, 2016 by 3:42 PM
import math
# def solution(A):
#     maxValue = A
#     lst = [int(i) for i in str(A)]
#     # print lst
#     unchanged = lst
#     new_number = []
#     # print len(lst)
#     for i in range(len(lst)-1):
#         new = int(math.ceil((lst[i] + lst[i+1]) / 2.0))
#         del lst[i]
#         # del lst[i]
#         # print lst
#         # del lst[i]
#         # lst.pop(i+1)
#         # lst.pop(i)
#         # lst.remove(lst[i])
#         # lst.remove(lst[i])
#         lst.insert(i,new)
#         del lst[i]
#         # print lst
#         y = int(''.join(str(x) for x in lst))
#         new_number.append(y)
#         # print new_number
#         lst = unchanged
#     return max(new_number)
#
#
# print solution(623315)
def solution(A):
    maxValue = 0
    counter = []
    xx = []
    alist = [int(i) for i in list(str(A))]
    # print alist
    unchanged = alist
    removed_values = []
    for i in range(len(alist)-1):
        rem_v = alist[i], alist[i+1]
        new =  int(math.ceil((alist[i] + alist[i + 1]) / 2.0))
        counter.append(new)
        removed_values.append(rem_v)
    # print removed_values

    for i in removed_values:
        alist.remove(i[0])
        alist.remove(i[1])
        print alist
        # x = alist.insert(i,counter[i])
        # xx.append(x)
        alist = unchanged
        # return xx


    # return counter

print solution(623315)