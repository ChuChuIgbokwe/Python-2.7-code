#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 02, 2016 by 3:19 PM

class BaseClass(object):
	def __init__(self):
		self.x = 5
		
	def printHam(self):
		print 'ham'
		
class subClass1(BaseClass):
	def __init__(self):
		self.x = 17
		
class subClass2(BaseClass):
	def __init__(self):
		super(subClass2, self).__init__()

	def printHam(self):
		print 'Ham2'
		
class child(subClass1,subClass2):
	def __init__(self, printHam=None):
		super(child,self).__init__()

if __name__ == '__main__':
	c = child()
	c.printHam()
	print c.x
	print BaseClass.__subclasses__() #Shows what classes are inheriting from your base cla




