#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 20, 2016 by 2:36 PM

def solution(A):
    # write your code in Python 2.7
    # count_list = []
    # for i in range(1,len(A) + 1):
    #     if sum(A[:i]) == sum(A[i+1:]):
    #         count_list.append(len(A[:i]))
    # return count_list[0]
    # pass
    equilibrium_positions = [len(A[:i]) for i in range(1,len(A) + 1) if sum(A[:i]) == sum(A[i+1:])]
    return equilibrium_positions

print solution([-1, 3, -4, 5, 1, -6, 2, 1] )
