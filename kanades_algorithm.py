#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 28, 2016 by 5:08 PM

def mssl(l):
    best = cur = 0
    for i in l:
        cur = max(cur + i, 0)
        best = max(best, cur)
    return best




print mssl([3,4,5])
print mssl([4, -2, -8, 5, -2, 7, 7, 2, -6, 5])
print mssl([-2,-3,-5])
print mssl([-2, -3, 4, -1, -2, 1, 5, -3])


def mssl(l):
    best = cur = 0
    curi = starti = besti = 0
    for ind, i in enumerate(l):
        if cur+i > 0:
            cur += i
        else: # reset start position
            cur, curi = 0, ind+1

        if cur > best:
            starti, besti, best = curi, ind+1, cur
    return starti, besti, best

print mssl([-2, -3, 4, -1, -2, 1, 5, -3])
# A variation of the problem that does not allow zero-length subarrays to be returned, in the case that the entire array
# consists of negative numbers, can be solved with the following code:

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
# print max_subarray([-2, -3, 4, -1, -2, 1, 5, -3])
print max_subarray([3,4,5])
# def KanadesAlgorithm(nums):


# print KanadesAlgorithm([-2,-3,4,-1,-2,1,5,-3])

# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
def maxSubArraySum(a, size):
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far
print maxSubArraySum([-2,-3,4,-1,-2,1,5,-3],8)