#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 26, 2016 by 10:17 PM

def bubble_sort(lst):
    nums = list(lst)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst

print bubble_sort([21,4,1,3,9,20,25,6,21,14])
# print bubble_sort([54,26,93,17,77,31,44,55,20])


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

print bubble_sort([21,4,1,3,9,20,25,6,21,14])
print bubble_sort([54,26,93,17,77,31,44,55,20])

# bubbleSort(alist)
# print(alist)


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               alist[i],alist[i + 1] = alist[i+1],alist[i]
       passnum = passnum-1
    return alist
print shortBubbleSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
print shortBubbleSort([20,30,40,90,50,60,70,80,100,110])


    # def bubble_sort(lst):
#     sorted = True
#     nums = list(lst)
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[j] < lst[i]:
#                 lst[j], lst[i] = lst[i], lst[j]
#     return lst

# def BubbleSortOptimized(alist):
#     len_tracker = len(alist)
#     for i in range(len_tracker):
#         end = len_tracker - i
#         swapped = False
#         for j in range(end - 1):
#             if alist[j] < alist[i]:
#                 alist[j], alist[i] = alist[i], alist[j]
#                 swapped = True
#         if not swapped:
#             break
#     return alist
# print BubbleSortOptimized([54,26,93,17,77,31,44,55,20])