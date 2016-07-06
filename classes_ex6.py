#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 23, 2016 by 2:35 PM

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

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def simplify(self):
        common = gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common

    def __add__(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __sub__(self, otherfraction):

        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __div__(self, other):
        newnum = self.num*other.den
        newden = self.den*other.num
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __mul__(self, otherfraction):
        newnum = self.num*otherfraction.num
        newden = self.den*otherfraction.den
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum == secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum < secondnum

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum > secondnum



myfraction = Fraction(12, 16)

print(myfraction)
myfraction.simplify()
print(myfraction)


myfraction = Fraction(3, 4)
yourfraction = Fraction(3, 4)
print(myfraction is yourfraction)

ourfraction = myfraction
print(myfraction is ourfraction)


myfraction = Fraction(3, 4)
yourfraction = Fraction(3, 4)
print(myfraction is yourfraction)
print(sameFraction(myfraction, yourfraction))

f1 = Fraction(1, 2)
f2 = Fraction(1, 4)

f3 = f1 + f2
print(f3)

def main():
    print 'main function'
    f = Fraction(1,3)
    g = Fraction(1,5)
    h = f+g
    print f.getNum()
    print f.getDen()
    j = Fraction(2,6)

    print h
    print 'subtraction: '
    print f-j
    print 'multiplication'
    print f*j
    print 'div'
    print f/j
    print g > f
    print g < f
    print g==f
    print f==j
    print f!=j

main()