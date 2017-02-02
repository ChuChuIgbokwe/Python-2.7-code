#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 15, 2016 by 8:33 PM

def one_away(aString,bString):
    if len(aString) > len(bString):
        longest_string = len(aString)
    else:
        aString,bString = bString,aString
        longest_string = len(aString)
    difference_counter = 0
    for i in bString:
        if i not in aString:
            difference_counter +=1
    if difference_counter == 1 or difference_counter == 0:
        return True
    else:
        return False

print one_away('pale','ple')
print one_away('pales','pale')
print one_away('pale','bale')
print one_away('pale','bake')
