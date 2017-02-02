#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 27, 2016 by 6:50 PM

def singleNumber(nums):
    # print nums.sort()
    # d = {key: value for (key, value) in enumerate(nums)}
    # return d
    for i in nums:
        if nums.count(i) == 1:
            return i
print singleNumber([3,4,5,3,7,8,8,4,7])