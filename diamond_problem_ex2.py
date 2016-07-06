#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 21, 2016 by 1:21 AM


'''
Only for those who are interested in Python version2:
To have the same inheritance behaviour in Python2 as in Python3, every class has to inherit from the class "object".
Our class A doesn't inherit from object, so we get a so-called old-style class, if we call the script with python2.
Multiple inheritance with old-style classes is governed by two rules: depth-first and then left-to-right.
If you change the header line of A into "class A(object):", we will have the same behaviour in both Python versions.
'''
class A:
	def m(self):
		print("m of A called")


class B(A):
	pass


class C(A):
	def m(self):
		print("m of C called")


class D(B, C):
	pass


x = D()
x.m()




