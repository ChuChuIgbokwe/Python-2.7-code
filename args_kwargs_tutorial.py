#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 02, 2016 by 1:15 PM

def Func(*args):
	for arg in args:
		print arg

# Func(1,2,3,54,'ham')
# print ''
# l = [1,2,3,54,'ham']
# Func(l)
# print ''
# Func(*l)

def Function(x = 234,y = 9):
	print x,y

Function()
Function(x = 456, y = 3)
print ''

# def F(**kwargs):
# 	for item in kwargs.items():
# 		print item
#
# F(x = 999,y = 54)

def F(*args, **kwargs):
	for arg in args:
		print arg
	for item in kwargs.items():
		print item

F(21,87,x = 456,y = 3,)

# for key, value in kwargs.items(): setattr(self, key, value)﻿

def elList(*args):
	'''
	Pirnt out individual elements of lists within lists
	:param args:
	:return:
	'''
	for argument in args:
		# print type(argument)
		if type(argument) == list:
			for thing in argument:
				print thing
		else:
			print argument

myList = ["hello", "how", "are", [1, 6], "you"]
elList(*myList)