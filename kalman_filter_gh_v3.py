#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 27, 2017 by 12:29 AM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys

weights = [158.0, 164.2, 160.3, 159.9, 162.1, 164.6,
169.6, 167.4, 166.4, 171.0, 171.2, 172.6]
time_step = 1 # day
weight_scale = 4/10
gain_scale = 1/3

def predict_using_gain_guess(weight, gain_rate):
    # store the filtered results
    estimates = []
    # most filter literature uses ’z’ for measurements
    for z in weights:
        # prediction step
        weight = weight + gain_rate * time_step
        gain_rate = gain_rate

        # update step
        residual = z - weight
        gain_rate = gain_rate + gain_scale *(residual / time_step)
        weight = weight + weight_scale * residual
        estimates.append(weight)

    # plot results
    n = len(weights)
    plt.xlim([1, n])
    plt.plot (range(1, n+1), estimates, '--', label='filter')
    plt.plot(range(1, n+1), weights, c='r', label='measurements')
    plt.plot([1, n],[160, 160+n],c='g', label='actual')
    plt.legend(loc=2)
    plt.xlabel('day')
    plt.ylabel('weight (lbs)')
    plt.ylim([0, 1])
    plt.show()
predict_using_gain_guess (weight=160, gain_rate=1.0)