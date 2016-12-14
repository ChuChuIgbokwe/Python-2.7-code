#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 26, 2016 by 4:05 PM

#removeDuplicates('aabbcc') = 'abc'

def removeDuplicates(word):
    if len(word) <= 1:
        return word
    elif word[0]==word[1]: #if two adjacent letters are the same, start from next letter
        return removeDuplicates(word[1:])
    else:
        return word[0] + removeDuplicates(word[1:])

print removeDuplicates('aabbbcccdddd')
