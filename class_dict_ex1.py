#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 10, 2016 by 1:13 AM

class Person:
    def __init__(self, id):
        self.id = id

obama = Person(100)

obama.__dict__['age'] = 49

print obama.age + len(obama.__dict__)

print obama.__dict__

