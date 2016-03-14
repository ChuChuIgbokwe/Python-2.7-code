#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 14, 2016 by 3:38 AM

'''
write a program that calculates the minimum and maximum score for each student.
Print out their name as well.
'''

f = open("studentdata.txt", "r")
aline = f.readline()

while aline:
	items = aline.split()
	print items[0]+"'s  maximum & minimum scores are ", max(items[1:]), min(items[1:])," respectively"
	aline = f.readline()

f.close()


# for aline in f:
#     items = aline.split()
#     print(items[0], "max is", max(items[1:]), "min is", min(items[1:]))
#
