#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 29, 2016 by 1:58 AM

def func():
	'''
	if __name__ == "__main__" explanation
	:return:
	'''
	print "func() in one.py"

print "top-level in one.py"

if __name__ == "__main__":
    print "one.py is being run directly"
else:
    print "one.py is being imported into another module"




