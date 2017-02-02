#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 15, 2016 by 6:18 PM
#
def replace_space(aString):
    return aString.replace(' ','%20')

print replace_space('Mr John Smith')

def another_replace(aString):
    for i in len(range(aString)):
        if aString[i] == ' ': # or chr(32)
            aString[i] = "%20"
    return aString

print replace_space('Mr John Smith')