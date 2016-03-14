#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 14, 2016 by 5:30 PM


# class IntContainer(object):
#     def __init__(self, i):
#         self.i = int(i)
#
#     def add_one(self):
#         self.i += 1
#
#
# class MyInt(int):
#     def __add__(self, other):
#         print "specializing addition"
#         return super(MyInt, self).__add__(other)
#
# i = MyInt(2)
# print(i + 2)
#
# ic = IntContainer(2)
# ic.add_one()
# print(ic.i)

class DoNothing(object):
    pass

d = DoNothing()
print type(d)
print type(DoNothing)