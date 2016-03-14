#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 10, 2016 by 1:46 PM

def decay(n):
	'''
	You have 1000 atoms of a radioactive material. 5% of the atoms decay
	every minute. How many atoms of the material you will still have after
	10 minutes?
	:param n:
	:return:
	'''

	for i in range(10):
		n = 0.95 * n
	return n

print decay(1000)
