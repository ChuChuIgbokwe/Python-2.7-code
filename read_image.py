#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on January 26, 2016 by 10:47 PM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
#import matplotlib as mpl
import cv2, os, sys

img = cv2.imread('ronaldo.jpg', 1)
hsv_img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
bgr_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# cv2.imshow('hsv image',hsv_img)
# cv2.imshow('bgr image',bgr_img)
# hsv_values = hsv_img
# h = hsv_values[0]
# print np.size(h)
# h,s,v = cv2.split(hsv_img)
# print hsv_img
cv2.imshow('CR7',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



