#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 02, 2016 by 1:45 PM

# class BaseClass(object):
# 	def printHam(self):
# 		print 'ham'
#
# class InheritingClass(BaseClass):
# 	pass
#
# x = InheritingClass() #create instance
# x.printHam()


class Character(object):
	def __init__(self,name):
		self.health = 100
		self.name = name

	def printName(self):
		print self.name

class Blacksmith(Character):
	def __init__(self,name,forgeName):
		super(Blacksmith, self).__init__(name) #access init from the base class we inherited from
		self.forge = Forge(forgeName)

class Forge:
	def __init__(self,forgeName):
		self.name = forgeName

bs = Blacksmith("Bob","Rick\'s forge")
bs.printName()
print bs.forge.name
print bs.health

