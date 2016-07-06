#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 18, 2016 by 9:59 PM

#Is it possible to have static methods in Python so I can call them without initializing a class, like:
#ClassName.StaticMethod ( )

ClassName.StaticMethod ( )
class MyClass(object):
    @staticmethod
    def the_static_method(x):
        print x

MyClass.the_static_method(2) # outputs 2



