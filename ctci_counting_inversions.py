#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 18, 2016 by 11:03 PM

def count_inversions(a):
    # counter = 0
    # for i in range(len(a)):
    #     for j in range(i + 1, len(a)):
    #         if a[i] > a[j]:
    #             counter += 1
    # return counter

    return sum([len(filter(lambda x: x < a[i],a[i:])) for i in xrange(len(a))])

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    print count_inversions(arr)
