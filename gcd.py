#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on January 28, 2016 by 12:21 AM


def gcd(a,b):
	'''
	Write a function called gcd that takes parameters a and b and returns their greatest common divisor.
One way to find the GCD of two numbers is based on the observation that if r is the remainder when
a is divided by b, then gcd(a, b) = gcd(b,r).
	'''
	while b != 0:
		(a, b) = (b, a % b)
	return a



print gcd(10,5)

# from fractions import gcd
# gcd(20,8)