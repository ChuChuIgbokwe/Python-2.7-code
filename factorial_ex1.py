#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 25, 2016 by 1:24 AM

def factorial(n):
	print "factorial has been called with n = ", n
	if n == 1:
		return 1
	else:
		res = n * factorial(n-1)
		print "intermediate result for ", n, " * factorial(" ,n-1, "): ",res
        return res


print factorial(4)

def iterative_factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result