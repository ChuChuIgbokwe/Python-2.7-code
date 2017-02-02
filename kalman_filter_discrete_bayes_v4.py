#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 27, 2017 by 12:29 AM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys

hallway = [1,0,1,0,0,1,0,1,0,0]
pos = np.array([.1]*10)
measurements = [1,0,1,0,0]

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

def predict(pos, move, p_correct, p_under, p_over):
    n = len(pos)
    result = np.array(pos, dtype=float)
    for i in range(n):
        result[i] = \
        pos[(i-move) % n] * p_correct + \
        pos[(i-move-1) % n] * p_over + \
        pos[(i-move+1) % n] * p_under
    return result

for m in measurements:
    pos = update(pos, m, .6, .2)
    pos = predict(pos, 1, .8, .1, .1)

# plt.bar(np.arange(len(pos)),pos)
# plt.ylim([0,1])
# plt.show()
# print(pos)


measurements = [0,1,0,1,0,0]
for i,m in enumerate(measurements):
    pos = update(pos, m, .6, .2)
    pos = predict(pos, 1, .8, .1, .1)
    plt.subplot(3, 2, i+1)
    plt.ylim([0,1])
    plt.title('step{}'.format(i+1))
    plt.bar(np.arange(len(pos)),pos,)
plt.show()