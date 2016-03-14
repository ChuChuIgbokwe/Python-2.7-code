#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 12, 2016 by 6:48 PM

def sum_of_squares(xs):
	'''
	Write a function sum_of_squares(xs) that computes the sum of the squares
	of the numbers in the list xs.
	For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:
	:param xs:
	:return:sum_of_list
	'''
	sum_of_list = [i**2 for i in xs]
	return sum_of_list

print sum_of_squares([2,3,4])

def count_odd_numbers(xs):
	count = 0
	for i in xs:
		if i%2 == 1:
			count += 1
	return count
print count_odd_numbers([1,2,3,4,5,6,7,8,9])
