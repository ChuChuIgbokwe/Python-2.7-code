#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on January 28, 2016 by 12:14 AM

'''
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power
that takes parameters a and b and returns True  if a is a power of b.
Note: you will have to think about the base case
'''

def is_power(a,b):
	if a%b == 0:
		print a,'is a power of ', b
		return True
	else:
		print a,'is not a power of ', b
		return False

is_power(8,4)



