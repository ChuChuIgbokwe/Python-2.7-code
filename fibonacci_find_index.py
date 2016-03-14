#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 25, 2016 by 4:10 PM

def fib(n):
	a,b = 0,1
	fib_list = []
	for i in range(n-1):
		fib_list.append(a)
		a,b = b,a+b
	return fib_list

def find_index(m):
	'''
	Write a recursive function find_index(), which returns the index of a number in the Fibonacci sequence,
	if the number is an element of this sequence and returns -1 if the number is not contained in it, i.e.
	:param n:
	:return: index or -1
	'''
	# print "Enter how many fibonacci numbers you want: "
	# n = int(raw_input())

	# fib_list = []
	# a,b = 0,1
	# for i in range(15):
	# 	fib_list.append(a)
	# 	a,b = b,a+b
	# print fib_list
	fib_list = fib(15)
	if m in fib_list:
		print m, "is at index ", fib_list.index(m)
		return fib_list.index(m)
	else:
		return -1


# print find_index(13)


print(" index of a |    a |     b | sum of squares | index ")
print("=====================================================")
for i in range(15):
	square = fib(i)**2 + fib(i+1)**2
	print( " %10d |  %3d |   %3d | %14d | %5d " % (i, fib(i), fib(i+1), square, find_index(square)))