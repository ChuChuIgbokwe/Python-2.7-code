#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 27, 2017 by 12:29 AM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys




def predict(pos, move, p_correct, p_under, p_over):
    n = len(pos)
    result = np.array(pos, dtype=float)
    for i in range(n):
        result[i] = \
        pos[(i-move) % n] * p_correct + \
        pos[(i-move-1) % n] * p_over + \
        pos[(i-move+1) % n] * p_under
    return result

#Singular Belief
# p = np.array([0,0,0,1,0,0,0,0])
# res = predict(p, 2, .8, .1, .1)
# print(res)


#Multiple Beliefs
p = np.array([0, 0, .4, .6, 0, 0, 0, 0])
res = predict (p, 2, .8, .1, .1)
print(res)

plt.bar(np.arange(len(res)),res)
plt.show()

