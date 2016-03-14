#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on January 28, 2016 by 3:36 AM

def filterFile(oldFile,newFile):
	'''
	the function makes a copy of oldFile, omitting any lines that
	begin with #
	:param oldFile:
	:param newFile:
	:return:
	'''
	f1 = open(oldFile,"r")
	f2 = open(newFile,"w")
	while True:
		text = f1.readline()
		if text == "":
			break
		if text == '#':
			continue
		f2.write(text)
	f1.close()
	f2.close()
	return



