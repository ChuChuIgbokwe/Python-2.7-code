#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 27, 2016 by 10:29 PM


## Function to find the maximum contiguous subarray
# def maxSubArraySum(a,size):
#
#     max_so_far = 0
#     max_ending_here = 0
#
#     for i in range(0, size):
#         max_ending_here = max_ending_here + a[i]
#         if max_ending_here < 0:
#             max_ending_here = 0
#
#         if (max_so_far < max_ending_here):
#             max_so_far = max_ending_here
#
#     return max_so_far
# Your previous Plain Text content is preserved below:
#
# Definition:
# * A subarray of an array [x0, x1, x2....] is any contiguous part of an array.
#
# Examples:
# * [x0, x1, x2] is a subarray of [x0, x1, x2, x3], but [x0, x2] is not.
# * [] is a subarray of any array
# * An array is a subarray of itself
#
# Goal:
# Write a function that takes as input an array of numbers, and returns the subarray that has the maximum sum.
#
# Examples:
#
# Input: []
# Output: []
#
# Input: [-4]
# Output: []
#
# Input: [1, -3, 1, 4]
# Output: [1, 4]
#
# Input: [12, -5, 6, -7, 18, 20]
# Output: [12, -5, 6, -7, 18, 20]
#
#
#
#
#
def MaxSubArray(array):
    initial_max = 0
    max_so_far = 0
    sub_array = []
    for i in range(len(array)):
        max_so_far = array[i]
        if max_so_far < 0:
            initial_max = 0
        else:
            sub_array.append(array[i])
    return sub_array



print MaxSubArray([12, -5, 6, -7, 18, 20])

# def get_max_sum_subset(x):
#     bestSoFar = 0
#     bestNow = 0
#     bestStartIndexSoFar = -1
#     bestStopIndexSoFar = -1
#     bestStartIndexNow = -1
#     for i in xrange(len(x)):
#         value = bestNow + x[i]
#         if value > 0:
#             if bestNow == 0:
#                 bestStartIndexNow = i
#             bestNow = value
#         else:
#             bestNow = 0
#
#         if bestNow > bestSoFar:
#             bestSoFar = bestNow
#             bestStopIndexSoFar = i
#             bestStartIndexSoFar = bestStartIndexNow
#
#     return bestSoFar, bestStartIndexSoFar, bestStopIndexSoFar

# def mssl(l):
#     best = cur = 0
#     curi = starti = besti = 0
#     for ind, i in enumerate(l):
#         if cur+i > 0:
#             cur += i
#         else: # reset start position
#             cur, curi = 0, ind+1
#
#         if cur > best:
#             starti, besti, best = curi, ind+1, cur
#     return starti, besti, best