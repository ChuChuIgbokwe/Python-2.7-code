#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 19, 2016 by 2:39 PM

from itertools import combinations


# def TwoSum(nums,target):
#     nums_copy = nums[:]
#     nums_copy.sort()
#     i = 0
#     while nums_copy[i] <= target:
#         d = target - nums_copy[i]
#         if d not in nums_copy:
#             i += 1
#         else:
#             if d != nums_copy[i]:
#                 return [nums.index(nums_copy[i]), nums.index(d)]
#             else:
#                 return [nums.index(nums_copy[i]), nums.index(d, nums.index(nums_copy[i]) + 1)]

def twoSum(self, nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i + 1]
        else:
            buff_dict[target - nums[i]] = i + 1


def twoSum(nums, target):
    dic = dict()

    for i, n in enumerate(nums):
        if target - n in dic:
            return [dic[target - n] + 1, i + 1]
        dic[n] = i

    return []

print twoSum([3, 2, 4],6)
print twoSum([0,4,3,0],0)
print twoSum([2,1,9,4,4,56,90,3],8)
print twoSum([5,75,25],100)


def twoSum(nums, target):
    dic = dict()

    for i, n in enumerate(nums):
        if target - n in dic:
            return [dic[target - n] + 1, i + 1]
        dic[n] = i

    return []


# print twoSum([5,75,25],100)