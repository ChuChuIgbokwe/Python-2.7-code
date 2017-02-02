#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 30, 2017 by 6:35 PM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys

def  StairCase(n):
    space = n
    hash = 1
    for i in range(n):
        print ('#'*hash).rjust(space)
        hash += 1

StairCase(6)