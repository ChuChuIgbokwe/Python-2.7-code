#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 28, 2016 by 6:11 PM

# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

def add_digits(n):
    while n > 9:
        n =  n%10 + n/10
    return n



print add_digits(384)