#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 20, 2016 by 12:26 PM

import math

# def isPrime(num):
#     # Returns True if num is a prime number, otherwise False.
#
#     # Note: Generally, isPrime() is slower than primeSieve().
#
#     # all numbers less than 2 are not prime
#     if num < 2:
#         return False
#
#     # see if num is divisible by any number up to the square root of num
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# print isPrime(6)

p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())

def is_prime(n):
    def isPrime(num):
        if num < 2 :
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
print is_prime(n)