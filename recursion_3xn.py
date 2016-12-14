#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 25, 2016 by 2:48 AM


def mult3(n):
	'''
	Think of a recusive version of the function f(n) = 3 * n, i.e. the multiples of 3
	:param n:
	:return: 3 * n
	'''

	print "factorial has been called with n = ", n
	if n == 1:
		return 3
	elif n == 0:
		return 0
	else:
		res = 3 + mult3(n-1)
		print "intermediate result for ", n, " * f(" ,n-1, "): ",res
        return res

print mult3(5)
print mult3.__doc__
