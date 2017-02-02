#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 29, 2016 by 12:29 AM
from collections import Counter
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) >= len(t):
        if len(Counter(s)-Counter(t)) == 0:
            print Counter(s),Counter(t)
            return True
        else:
            return False
    else:
        if len(Counter(t) - Counter(s)) == 0:
            print Counter(s), Counter(t)
            return True
        else:
            return False


def isAnagram1(self, s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2


def isAnagram2(self, s, t):
    dic1, dic2 = [0] * 26, [0] * 26
    for item in s:
        dic1[ord(item) - ord('a')] += 1
    for item in t:
        dic2[ord(item) - ord('a')] += 1
    return dic1 == dic2

def isAnagram3( s, t):
    return sorted(s) == sorted(t)

print isAnagram3('a','ab')
