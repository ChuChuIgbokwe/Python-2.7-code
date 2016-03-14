#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 02, 2016 by 3:51 PM

from abc import ABCMeta, abstractmethod

class BaseClass(object):
	__metaclass__ = ABCMeta

	@abstractmethod #decoration dynamically alter classes without inheritance or subclasses
	def printHam(self):
		pass

class InClass(BaseClass):
	def printHam(self):
		print 'ham'

#x = BaseClass() #You cannot instantiate an abstract class

x = InClass()
x.printHam()




