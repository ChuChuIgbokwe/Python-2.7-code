#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on January 27, 2016 by 4:17 PM


def b(z):
	prod = a(z,z)
	print z, prod
	return prod #passed to function c

def a(x,y):
	x = x + 1
	return x + y

def c(x,y,z):
	total = x + y + z
	square = b(total)**2 #(total + total + 1)**2
	return square

x = 1
y = x + 1
print c(x,y+3,x+y)



