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

# def normalize(p):
#     s = sum(p)
#     for i in range (len(p)):
#         p[i] = p[i] / s
#
# def update (pos, measure, p_hit, p_miss):
#     q = np.array(pos, dtype=float)
#     for i in range(len(hallway)):
#         if hallway[i] == measure:
#             q[i] = pos[i] * p_hit
#         else:
#             q[i] = pos[i] * p_miss
#     normalize(q)
#     return q
# pos = np.array([0.2]*10)
# reading = 1 # 1 is ’door’
# pos = update (pos, 1, .6, .2)
# print pos
# print 'probability of door =', pos[0]
# print 'probability of wall =', pos[2]
# print  "sum = ", sum(pos)
# plt.bar(np.arange(len(pos)),pos)
# plt.show()


def perfect_predict(pos, move):
    """ move the position by ’move’ spaces, where positive is to the right, and
    is to the left
    """
    n = len(pos)
    result = np.array(pos, dtype=float)
    for i in range(n):
        result[i] = pos[(i-move) % n]
    return result

pos = np.array([.4, .1, .2, .3])
print 'pos before predict =', pos
plt.figure(1)
plt.subplot(211)
plt.bar(np.arange(len(pos)), pos)
plt.title("Before prediction")
plt.ylim([0,1])
# plt.show()

pos = perfect_predict(pos, 1)
print 'pos after predict =', pos
plt.subplot(212)
plt.bar(np.arange(len(pos)), pos)
plt.title("After prediction")
plt.ylim([0,1])
plt.show()


pos_before_predict = [ 0.4,0.1, 0.2 ,0.3]
pos_after_predict = [ 0.3, 0.4, 0.1, 0.2]