#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 21, 2016 by 2:59 AM

#super() can be used only in the new-style classes, which means the root class needs to inherit from the 'object' class
# class SomeClass(object):
#     def __init__(self):
#         ....
# not
#
# class SomeClass():
#     def __init__(self):
#         ....

class A(object):
	def m(self):
		print("m of A called")


class B(A):
	def m(self):
		print("m of B called")
		super(B,self).m()


class C(A):
	def m(self):
		print("m of C called")
		super(C,self).m()


class D(B, C):
	def m(self):
		print("m of D called")
		super(D,self).m()

x = D()
x.m()
print D.mro() #method resolution order