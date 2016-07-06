#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 18, 2016 by 10:41 AM

class MySingleton(object):
	_instance = None
	def __new__(cls, *args, **kwargs): #constructor
	# def __new__(self):
		if not cls._instance: #check if instance has been set
			cls._instance = super(MySingleton,cls).__new__(cls,*args, **kwargs) #create instance
			cls.y = 10
			return cls._instance #every instance in future will be pointing to the exact same one created


x = MySingleton()
print x.y
x.y = 20

z = MySingleton()
print z.y

