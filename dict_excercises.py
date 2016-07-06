#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 15, 2016 by 1:24 AM
import string
def count_letters():
	'''
	Write a program that allows the user to enter a string. It then prints a
	table of the letters of the alphabet in alphabetical order which occur in
	the string together with the number of times each letter occurs.
	Case should be ignored.
	:return:
	'''

	str = raw_input("Enter a string: ")
	str_dict = dict()
	str = str.lower()
	for i in str:
		 #remove punctuation and spaces
		if i in string.punctuation or i == ' ':
			continue
		else:
			count = str.count(i)
			str_dict[i] = count

	for (k,v) in sorted(str_dict.items()):
		print  k, v


count_letters()


