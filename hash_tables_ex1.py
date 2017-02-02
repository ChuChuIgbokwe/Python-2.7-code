#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 15, 2016 by 5:25 PM

def hash(astring, tablesize):
    sum = 0
    for i in range(len(astring)):
        sum += ord(astring[i])

    return sum % tablesize

print hash('cat',11)