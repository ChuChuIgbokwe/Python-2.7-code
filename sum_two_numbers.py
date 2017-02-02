#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 27, 2016 by 8:21 PM

def getSum(a,b):
    if b == 0:
        return a
    carry = (a & b) <<1
    sum_ = a ^ b
    return getSum(sum_, carry)

def getSum(a,b):
    s = a
    while b!=0:
        s = a^b #calculate sum of a and b without thinking the carry. Sum by XOR
        b = (a&b) << 1 #calculate the carry
        a = s #add sum(without carry) and carry
    return s


def add(a, b):
    while a != 0:
        #      v carry portion| v sum portion
        a, b = ((a & b) << 1),  (a ^ b)
        # print b, a
    return b

def add_signed_numbers(a, b):
    while a != 0:
        #      v carry portion| v sum portion
        a, b = ((a & b) << 1),  (a ^ b)
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        print b, a
    return b

print getSum(11,4)
