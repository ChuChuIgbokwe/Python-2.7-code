#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 27, 2017 by 12:19 AM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys

weights = [158.0, 164.2, 160.3, 159.9, 162.1, 164.6,
169.6, 167.4, 166.4, 171.0, 171.2, 172.6]
# plt.plot(weights)
# plt.xlabel('day')
# plt.ylabel('weight (lbs)')
# plt.show()

# ave = np.sum(weights) / len(weights)
# plt.plot(weights,label='weights')
# plt.plot([0,12], [ave,ave], c='r', label='hypothesis')
# plt.xlabel('day')
# plt.ylabel('weight (lbs)')
# plt.legend(loc='best')
# plt.show()

xs = range(len(weights))
line = np.poly1d(np.polyfit(xs, weights, 1))
plt.plot(weights, label='weights')
plt.plot (xs, line(xs), c='r', label='hypothesis')
plt.xlabel('day')
plt.ylabel('weight (lbs)')
plt.legend(loc='best')
plt.ylim([0,1])
plt.show()