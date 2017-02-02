#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 04, 2016 by 10:31 PM

import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('ronaldinho.jpg')
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
#
# plt.imshow(hist,interpolation = 'nearest')
# plt.show()


img = cv2.imread('ronaldinho.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist( [hsv], [0, 1], None, [8, 8], [0, 180, 0, 256] )
hist_norm = cv2.normalize(hist,hist,0,1,cv2.NORM_MINMAX)#.flatten()


img1 = cv2.imread('ronaldo.jpg')
hsv1 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
hist1 = cv2.calcHist( [hsv1], [0, 1], None, [8, 8], [0, 180, 0, 256] )
hist1_norm = cv2.normalize(hist1,hist1,0,1,cv2.NORM_MINMAX)#.flatten()
k = cv2.compareHist(hist_norm,hist1_norm,cv2.cv.CV_COMP_CHISQR)
print k

plt.imshow(hist_norm,interpolation = 'nearest')
fig = plt.figure()
plt.imshow(hist1_norm,interpolation = 'nearest')
plt.show()



