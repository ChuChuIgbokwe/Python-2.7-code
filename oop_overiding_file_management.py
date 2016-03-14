#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 02, 2016 by 2:30 PM

class BaseClass(object):
	def __init__(self):
		self.x = 10

	def test(self):
		print 'ham'

class InClass(BaseClass):
	def __init__(self):
		super(InClass,self).__init__()
		self.x = 20 #due to inheritance the default value of this is 10
	def test(self):
		print 'hammer time'

i = InClass()
print i.x
i.test()

j = BaseClass()
j.test()
print j.x


print BaseClass.__subclasses__() #Shows what classes are inheriting from your base class



