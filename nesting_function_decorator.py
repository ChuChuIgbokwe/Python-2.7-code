#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 18, 2016 by 9:15 AM

def outside(x =5):
	# x = 5 #global to printHam
	def printHam(): #creating an obbject within the function
		print x
	return printHam #rturning the object

myFunc =outside(7)
myFunc() #
# print x  will crash the program

def addOne(myFunc):
	def addOneInside(*args, **kwargs):
		return myFunc(*args, **kwargs) + 1
	return addOneInside()

@addOne #overriding oldFunc. the decorator passes oldFunc 'automatically' into addOne,
def oldFunc(x = 3245):
	return x

# newFunc = addOne(oldFunc)
# print oldFunc(), newFunc

# overriding oldFunc
# oldFunc = addOne(oldFunc)
# print oldFunc

print oldFunc