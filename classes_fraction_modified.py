#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 26, 2016 by 11:58 AM

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

def sameFraction(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())

class Fraction:

    def __init__(self, top, bottom):

        try:
            self.num = int(top)        # the numerator is on top
            self.den = int(bottom)     # the denominator is on the bottom

        except ValueError:
            print " You didn't instantiate the class with integers"

        common = gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):

        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum , newden)

    def __div__(self, other):
        newnum = self.num*other.den
        newden = self.den*other.num

        return Fraction(newnum , newden)

    def __mul__(self, otherfraction):
        newnum = self.num*otherfraction.num
        newden = self.den*otherfraction.den

        return Fraction(newnum , newden )

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum == secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum >= secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum <= secondnum

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum <> secondnum

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum > secondnum

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __iadd__(self, other):
        x = self.__add__(other)

        return x



f = Fraction(1,-3)
g = Fraction(1,-5)
print f>g
print f<=g
h = sum([f,g])
print h
print f++ g
# h = Fraction('x',4)
# print h
