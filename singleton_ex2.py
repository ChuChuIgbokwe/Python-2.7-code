#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 18, 2016 by 11:44 AM

def singleton(myClass):
	instances = {}
	def getInstance(*args,**kwargs):
		if myClass not in instances:
			instances[myClass] = myClass(*args,**kwargs)
		return instances[myClass]
	return getInstance()

@singleton
class TestClass(object):
	pass

x = TestClass




