#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 15, 2016 by 1:08 PM

from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


# print(parChecker('{{([][])}()}'))
# print(parChecker('[{()]'))
print parChecker('"{[}]}')
print parChecker('{}[]()')

def braces(values):
    s = Stack()
    balanced = True
    index = 0
    while index < len(values) and balanced:
        symbol = values[index]
        if symbol == "(" or symbol == "[" or symbol == '{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return "YES"
    else:
        return "NO"


from collections import Counter
def braces(values):
    b = Counter(values)
    answer = ['YES','NO']
    if b['{'] == b['}'] and b['('] == b[')'] and b['['] == b[']']:
        return 'YES'
    else:
        return 'NO'

print braces('{}[]()')
print braces("{[}]}")