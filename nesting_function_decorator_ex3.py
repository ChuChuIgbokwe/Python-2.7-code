#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 18, 2016 by 9:53 AM


def addSandwich(meat):
	def makeSandwich():
		return meat() + " sandwich"
	return makeSandwich()

@addSandwich
def printHam(x = 'Turkey'):
	# x = "Ham"
	return x

print printHam



