#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 19, 2016 by 2:06 PM


# def square_numbers(nums):
# 	result = []
# 	for i in nums:
# 		result.append(i*i)
# 	return result

#Generator Conversion
def square_numbers(nums):
	for i in nums:
		yield (i*i)

my_nums = square_numbers([1,2,3,4,5]) #nothing computed or stored in memory
# for i in range(5):
# 	print next(my_nums)
# my_nums = [x*x for x in [1,2,3,4,5]] #list comprehension
my_nums = (x*x for x in [1,2,3,4,5]) #generator. parenthesis makes it a generator
print my_nums
# print next(my_nums) #next asks for the next result

for num in my_nums:
	print num

