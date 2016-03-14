#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 14, 2016 by 3:21 AM

'''
write a program that calculates the average grade for each student, and print out the student’s name along with
their average grade.
'''

f = open("studentdata.txt", "r")
aline = f.readline()

while aline:
	items = aline.split()
	total_sum = 0
	for i in items[1:]:
		total_sum += int(i)
	avg = float(total_sum) / len(items[1:])
	print items[0]+"'s  average score is ", avg
	aline = f.readline()

f.close()