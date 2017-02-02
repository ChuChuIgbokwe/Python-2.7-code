#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 27, 2016 by 5:27 PM

'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x^y).count('1')

print hammingDistance(1,4)

# def binary(decimal) :
#     otherBase = ""
#     while decimal != 0 :
#         otherBase  =  str(decimal % 2) + otherBase
#         decimal    /=  2
#     return otherBase
#
# def toBinary(n):
#     return ''.join(str(1 & int(n) >> i) for i in range(64)[::-1])
#
# def int2bin(i):
#     if i == 0: return "0"
#     s = ''
#     while i:
#         if i & 1 == 1:
#             s = "1" + s
#         else:
#             s = "0" + s
#         i /= 2
#     return s
#
# print  int2bin(1)
#
# s = "{0:b}".format(4)
# b = [int(i) for i in s]