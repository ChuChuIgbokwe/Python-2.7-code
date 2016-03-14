#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on January 27, 2016 by 3:07 PM

# def factorial(n):
# 	if n == 0:
# 		print 'returning 1'
# 		return 1
# 	else:
# 		recurse = n * factorial(n-1)
# 		print 'return', recurse
# 		return n * factorial(n-1)
#
# factorial(5)

def factorial(n):
	space = ' ' * (4*n)
	print space, 'factorial', n
	if n == 0:
		print space, 'returning 1'
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		print space, 'returning', result
		return result

factorial(5)
