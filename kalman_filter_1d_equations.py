#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 29, 2017 by 1:19 AM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys

def multiply(mu1, var1, mu2, var2):
    mean = (var1*mu2 + var2*mu1) / float(var1+var2)
    variance = 1 / (1/float(var1) + 1/float(var2))
    return (mean, variance)

def update(mean, variance, measurement, measurement_variance):
    return multiply(mean, variance, measurement, measurement_variance)

def predict(pos, variance, movement, movement_variance):
    return (pos + movement, variance + movement_variance)

