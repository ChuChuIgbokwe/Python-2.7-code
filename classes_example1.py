#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 02, 2016 by 11:49 AM

# class Ph:
# 	def __init__(self):
# 		self.y = 5
# 		self.printHam()
# 	def printHam(self):
# 		print 'ham'
#
# x = Ph()
# # x.printHam()
# # print x.y

class Hero:
	'''
	A hero who is allergic to apples
	'''
	def __init__(self,name):
		self.name = name
		self.health = 100

	def eat(self,food):
		if food =='apple':
			self.health-=100
		elif food == 'ham':
			self.health +=20
		if self.health == 0:
			print 'Bob is dead'

Bob = Hero("Bob")
print Bob.name
print Bob.health
Bob.eat('apple')
print Bob.health

