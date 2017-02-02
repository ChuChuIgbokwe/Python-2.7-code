#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 27, 2016 by 3:31 PM

from collections import Counter
def is_anagram(a,b):
    if len(a) != len(b):
         return False
    return  Counter(a) == Counter(b)

def is_permutation(a, b):
    return len(a) == len(b) and Counter(a) == Counter(b)