#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 13, 2016 by 4:52 AM

def applyRules(lhch):
    rhstr = ""
    if lhch == 'A':
        rhstr = 'BAB'   # Rule 1
    elif lhch == 'B':
        rhstr = 'AB'  # Rule 2
    else:
        rhstr = lhch    # no rules apply so keep the character

    return rhstr


def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr


def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

print(createLSystem(2, "A"))




