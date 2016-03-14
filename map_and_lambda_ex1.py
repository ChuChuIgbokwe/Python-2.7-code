#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 09, 2016 by 11:11 PM

items = [1,2,3,4,5]

def squared(x):
	squared_list = []
	for i in x:
		squared_list.append(i**2)
	return squared_list

print squared(items)


def sqr(x):
	return x**2

print "mapped version ",list(map(sqr,items))

print "lambda version ",list(map((lambda x:x**2),items))
print ''

def square(x):
	return x**2

def cube(x):
	return x**3

funcs = [square,cube]
for r in range(5):
	value = map(lambda x: x(r),funcs)
	print value


def mymap(aFunc, aSeq):
	'''
	Because using map is equivalent to for loops, with an extra code we can always
	write a general mapping utility
	:param aFunc:
	:param aSeq:
	:return: result
	'''
	result = []
	for x in aSeq:
		result.append(aFunc(x))
	return result

print "in-built map function"
print list(map(sqr, [1, 2, 3]))
print "equivalent mapping function"
print mymap(sqr, [1, 2, 3])