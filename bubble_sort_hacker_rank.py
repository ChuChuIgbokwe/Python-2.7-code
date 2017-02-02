#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 18, 2016 by 7:50 PM

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

def bubble_sort(lst):
    numSwaps = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
                numSwaps += 1
    return  'Array is sorted in %d swaps.\nFirst Element: %d \nLast Element: %d \n'%(numSwaps,lst[0],lst[-1])


print bubble_sort(a)
