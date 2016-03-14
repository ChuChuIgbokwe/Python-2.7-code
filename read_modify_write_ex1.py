#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 14, 2016 by 2:00 AM

infile = open("qbdata.txt", "r")
outfile = open("qbnames.txt", "w")

aline = infile.readline()
while aline:
	items = aline.split()
	dataline = items[1] + ', ' + items[0]
	outfile.write(dataline +  '\n')
	aline = infile.readline()

infile.close()
outfile.close()




