#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 21, 2016 by 1:28 AM

class A:
	def m(self):
		print("m of A called")


class B(A):
	def m(self):
		print("m of B called")


class C(A):
	def m(self):
		print("m of C called")


# class D(B, C):
# 	def m(self):
# 		print("m of D called")
#
#
# x= D()
# x.m()
# B.m(x)
# C.m(x)
# A.m(x)

# Now let's assume that the method m of D should execute the code of m of B, C and A as well, when it is called.
# We could implement it like this:
class D(B,C):
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)
        A.m(self)

x = D()
x.m()