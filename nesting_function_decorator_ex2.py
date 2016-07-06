#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 18, 2016 by 9:47 AM


# The entire purpose of a decorator is to modify the value  that is returned by a newly defined function.
# So if i want the string 'Pie' concatenated to each word i input, i would first create a function that could return
# only the word i input. ie, Always make sure to return something.
# Then i would define another function above that could modify this value and again return it.
# Both the function can only return values.

def concPie(addWord):
    """This Function Was Created Second"""
    def concPieInside():
        return addWord() + "Pie"
    return concPieInside

@concPie
#The Code Below Was Created First
def word():
    inp = raw_input("Type any word you like: ")
    return str(inp)

print word()




