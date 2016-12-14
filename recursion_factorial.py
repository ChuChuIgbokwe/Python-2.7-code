#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 26, 2016 by 3:49 PM

def factorial(number):
    if number <= 1:
        return 1
    else:
        # print number
        return number * factorial(number - 1)

print factorial(5)