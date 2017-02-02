#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 01, 2017 by 1:57 PM

def mySqrt(x):
    if x <= 1:
        return x

    l, r = 0, x // 2

    while l < r:
        mid = l + (r - l + 1) / 2

        tmp = mid * mid

        if tmp <= x:
            l = mid
        else:
            r = mid - 1

    return r

print mySqrt(65)