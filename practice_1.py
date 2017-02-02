#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 23, 2016 by 3:36 PM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys

"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


class Classy(object):

    def __init__(self):
        self.items = []

    def addItem(self, string):
        return self.items.append(string)

    def getClassiness(self):
        classiness_dict = {"tophat": 2, "bowtie": 4, "monocle": 5}
        count = 0
        if len(self.items) > 0:
            for i in range(len(self.items)):
                if classiness_dict.has_key(self.items[i]):
                    count += classiness_dict.get(self.items[i])
            return count
        else:
            return count



# Test cases
me = Classy()

# Should be 0
print me.getClassiness()

me.addItem("tophat")
# Should be 2
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print me.getClassiness()

me.addItem("bowtie")
# Should be 15
print me.getClassiness()