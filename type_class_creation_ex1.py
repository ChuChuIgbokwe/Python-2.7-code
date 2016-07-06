#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 18, 2016 by 12:19 PM

# class MyClass(object):
# 	def __init__(self):
# 		self.x = 5

def printHam(self):
	print "ham"

TypeClass = type("TypeClass",(object,),{"x":5, "printHam":printHam})

# m = MyClass()
t = TypeClass()

print  t.x, t.printHam()