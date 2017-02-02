#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 27, 2017 by 12:29 AM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys
plt.rcdefaults()

pos = np.array([0.333, 0.333, 0., 0., 0., 0., 0., 0., 0.333, 0.])
hallway = np.array([1, 1, 0, 0, 0, 0, 0, 0, 1, 0])
# left = np.arange(len(pos))
# plt.bar(left,pos)
# plt.show()

def normalize(p):
    s = sum(p)
    for i in range (len(p)):
        p[i] = p[i] / s

def update (pos, measure, p_hit, p_miss):
    q = np.array(pos, dtype=float)
    for i in range(len(hallway)):
        if hallway[i] == measure:
            q[i] = pos[i] * p_hit
        else:
            q[i] = pos[i] * p_miss
    normalize(q)
    return q
pos = np.array([0.2]*10)
reading = 1 # 1 is ’door’
pos = update (pos, 1, .6, .2)
print pos
print 'probability of door =', pos[0]
print 'probability of wall =', pos[2]
print  "sum = ", sum(pos)
plt.bar(np.arange(len(pos)),pos)
plt.ylim([0,1])
plt.show()