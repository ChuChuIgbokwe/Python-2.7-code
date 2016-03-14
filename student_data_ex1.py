#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 14, 2016 by 2:24 AM

'''
write a program that prints out the names of students that have more than six quiz scores.
'''
f = open("studentdata.txt", "r")

for aline in f:
	items = aline.split()
	if len(items[1:]) > 6:
		print items[0]


f.close()

