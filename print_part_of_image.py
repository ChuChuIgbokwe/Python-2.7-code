#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 05, 2016 by 3:07 AM

import numpy as np
import cv2

# 200 x 80 region of interest window at the bottom of the screen
img = cv2.imread('ronaldo.jpg')
w,h = img.shape[:2]
w_w = 200
w_h = 80
# img_part = img[(w/2.0 - w_w/2.0):(w/2.0 + w_w/2.0),(h - w_h):h]
img_part = img[(h/2.0 - w_h/2.0):(h/2.0 + w_h/2.0),(w - w_w):w]

width, height = img_part.shape[:2]
print width, height
print w,h

cv2.namedWindow('window',1)
cv2.imshow('part',img_part)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


