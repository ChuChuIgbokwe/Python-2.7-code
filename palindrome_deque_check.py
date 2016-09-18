#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 15, 2016 by 4:30 PM

# from pythonds.basic.deque import Deque
#
# def palchecker(aString):
#     chardeque = Deque()
#
#     for ch in aString:
#         chardeque.addRear(ch)
#
#     stillEqual = True
#
#     while chardeque.size() > 1 and stillEqual:
#         first = chardeque.removeFront()
#         last = chardeque.removeRear()
#         if first != last:
#             stillEqual = False
#
#     return stillEqual
#
# print(palchecker("lsdkjfskf"))
# print(palchecker("radar"))

from collections import deque

def palchecker(aString):
    chardeque = deque()

    for ch in aString:
        chardeque.appendleft(ch)

    stillEqual = True

    while len(chardeque) > 1 and stillEqual:
        first = chardeque.pop()
        last = chardeque.popleft()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
# print(palchecker("radar"))

