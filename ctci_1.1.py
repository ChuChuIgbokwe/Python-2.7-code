#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 15, 2016 by 5:37 PM

def is_unique(astring):
    '''
    an algorithm to determin if a string has all unique characters
    :param astring:
    :return:
    '''
    count_list = [astring.count(i) for i in astring if astring.count(i) > 1 ] #O(N) where N = length of astring
    if count_list == []:
        return True
    else:
        return False


print is_unique('qwerty') #True
print is_unique('qqwwerty') #False