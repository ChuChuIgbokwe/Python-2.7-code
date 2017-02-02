#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 28, 2016 by 11:37 PM

def wordPattern(pattern,string):
    k = ' '.join(pattern).split()
    v = string.split()
    if len(set(k)) != len(set(v)):
        return False
    else:
        d = dict(zip(k,v))
        s = [d[i] for i in k]
        return s == v


print wordPattern("abba","dog cat cat dog" )
print wordPattern("abba","dog cat cat fish")
print wordPattern("aaaa", "dog cat cat dog")
print wordPattern("abba", "dog dog dog dog")