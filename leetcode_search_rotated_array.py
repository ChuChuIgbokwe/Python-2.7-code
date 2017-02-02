#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 01, 2017 by 2:11 PM

def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) / 2

        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[l]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1

print search([0, 1, 2, 8, 13, 17, 19, 32, 42,],55)