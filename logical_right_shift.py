#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 19, 2016 by 1:30 PM

def rshift(val, n): return val>>n if val >= 0 else (val+0x100000000)>>n

import numpy
numpy.right_shift(1000, 3)