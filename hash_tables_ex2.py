#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 15, 2016 by 5:29 PM

def hash(astring, tablesize):
    '''
    positional value is used as a weighing factor
    :param astring:
    :param tablesize:
    :return:
    '''
    sum = 0
    weight = 1
    for i in range(len(astring)):
        sum += ord(astring[i]) * weight
        weight +=1
    return sum % tablesize

print hash('cat',11)