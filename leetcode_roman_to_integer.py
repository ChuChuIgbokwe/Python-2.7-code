#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 29, 2016 by 10:31 PM

def romanToInt( s):
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    roman_ixc = {'I':5, 'X':50, 'C':500}
    value = 0
    for i in reversed(s):
        if i in roman_ixc and value >= roman_ixc[i]:
            value -= roman_dict[i]
        else:
            value += roman_dict[i]
    return value
print romanToInt('MMMCMXVIII')

def romanToInt(s):
    map={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    pre=100000
    ret=0
    for i in s:
        cur=map[i]
        if cur>pre:
            ret=ret-pre-pre+cur
        else:
            ret=ret+cur
        pre=cur
    return ret
print romanToInt('MMDCCLXVI')


def romanToInt(s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]

print romanToInt('MCDLXXXIX')