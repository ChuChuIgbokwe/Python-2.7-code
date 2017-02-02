#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 26, 2016 by 9:31 PM

def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        print position
        return get_fib(position-1) + get_fib(position-2)

# Test cases
print get_fib(5)
# print get_fib(9)
# print get_fib(11)
# print get_fib(0)
