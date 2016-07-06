#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 15, 2016 by 10:59 PM

def ack(m, n):
	'''
	Write a function named ack that evaluates Ackerman's function. Use your
 	function to evaluate ack(3, 4), which should be 125. What happens for larger
 	values of m and n?
	:param m:
	:param n:
	:return:
	'''
	if m == 0:
		return n + 1
	elif n == 0:
		return ack(m - 1, 1)
	else:
		return ack(m - 1, ack(m, n - 1))

print ack(2,4)




