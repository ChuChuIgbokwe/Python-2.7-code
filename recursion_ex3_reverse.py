#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 15, 2016 by 7:52 PM

def reverse_string(s):
	'''
	Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.
	:param n:
	:return:
	'''
	if s == "":
		return s
	else:
		return reverse_string(s[1:]) + s[0]


n= raw_input("Enter a string: ")
print reverse_string(n)
