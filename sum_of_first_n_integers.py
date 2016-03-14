#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 25, 2016 by 2:53 AM

# def sum_to(n):
# 	'''
# 	Write a recursive Python function that returns the sum of the first n integers.
# 	(Hint: The function will be similiar to the factorial function!)
# 	:param n:
# 	:return:
# 	'''
# 	print "factorial has been called with n = ", n
# 	if n == 0: #RuntimeError: maximum recursion depth exceeded if you use 1
# 		return 0
# 	else:
# 		res = n + sum_to(n-1)
# 		print "intermediate result for ", n, " * factorial(" ,n-1, "): ",res
#         return res
#
#
# print sum_to(50)
