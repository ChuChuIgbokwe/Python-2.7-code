#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on January 27, 2016 by 2:43 PM

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

#n = int(input('Enter a number: '))
print fibonacci(7)



