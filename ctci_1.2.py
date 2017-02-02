#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 15, 2016 by 6:06 PM

def is_permutation(astring,bstring):
    '''
    Given two strings write a method to determine if one is a permutation of the other
    :param astring:
    :param bstring:
    :return:
    '''

    if len(astring) < len(bstring):
        return astring in bstring
    else:
        return bstring in astring

print is_permutation('chat', 'flat')

#Methods:
# 1. sort the strings and compare each index
# 2. check if both strings have the same character count