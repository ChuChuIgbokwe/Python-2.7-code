#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 15, 2016 by 1:35 PM

from pythonds.basic.stack import Stack

def divideBy2(decNumber):
    '''
    convert a decimal number to it's binary equivalent
    '''
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        # we read conversions from top to bottom mathematically,so we have to pop elements off the stack
        # to get the right answer. i.e the when dividing we get 010101 and that's the order of elements in the stack
        # popping elements geives us the right answe
        binString = binString + str(remstack.pop())

    return binString #101010

print(divideBy2(42))