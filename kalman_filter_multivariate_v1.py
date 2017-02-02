#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 29, 2017 by 3:47 AM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys

import filterpy.filterpy.stats as stats

P = np.array([[2,0],[0,2]])
plt.subplot(131)
stats.plot_covariance_ellipse((2,7), cov=P, facecolor='g', alpha=0.2,
title='|2 0|\n|0 2|')

plt.subplot(132)
P = np.array([[2,0],[0,9]])
stats.plot_covariance_ellipse((2,7), P, facecolor='g', alpha=0.2,
title='|2 0|\n|0 9|')

plt.subplot(133)
P = np.array([[2,1.2],[1.2,2]])
stats.plot_covariance_ellipse((2,7), P, facecolor='g', alpha=0.2,
title='|2 1.2|\n|1.2 2|')

plt.tight_layout()
plt.show()