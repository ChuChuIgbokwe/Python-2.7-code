#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 10, 2016 by 2:55 AM

def getinput():
	'''
	0 is returned from getinput. Remember that both 0, None, empty sequences and some other forms all evaluate
	to False in truth testing.
	:return:
	'''
    print "0: start"
    print "1: stop"
    print "2: reset"
    x = raw_input("selection: ")
    try:
        num = int(x)
        if num > 2 or num < 0:
            return None
        return num
    except:
        return None

num = getinput()
if not num:
    print "invalid"
else:
    print "valid"



