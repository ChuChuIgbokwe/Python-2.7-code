#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 21, 2016 by 1:07 AM
'''
		 A
	    / \
	   B   C
	   	\ /
		 D
'''
class A(object):
	def m(self):
		print 'm of A called'

class B(A):
	def m(self):
		print "m of B called"

class C(A):
	def m(self):
		print ("m of C called")

class D(B,C): #If we transpose the order of the classes in the class header of D in "class D(C,B):", x.m() => "m of C called"
	pass

x= D()
x.m() #m of B called

