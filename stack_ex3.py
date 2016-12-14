#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 10, 2016 by 9:57 PM

from pythonds.basic.stack import Stack

def revstring(mystr):
    '''
    Write a function revstring(mystr) that uses a stack to reverse the characters in a string.
    :param mystr:
    :return:
    '''
    s = Stack()
    reversed_string = ''
    for i in mystr:
        s.push(i)
    for j in range(len(mystr)):
        reversed_string += s.pop()
    return reversed_string

print revstring('apple')