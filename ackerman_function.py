#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on January 27, 2016 by 4:42 PM


def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))

print ackermann(3, 4)

def naive_ackermann(m, n):
    # global calls
    # calls += 1
    if m == 0:
        return n + 1
    elif n == 0:
        return naive_ackermann(m - 1, 1)
    else:
        return naive_ackermann(m - 1, naive_ackermann(m, n - 1))

print naive_ackermann(3,4)