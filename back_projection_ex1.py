#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 05, 2016 by 1:11 AM

import cv2
import numpy as np


#roi is the object or region of object we need to find
roi = cv2.imread('balon_dor_small.jpg')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

#target is the image we search in
target = cv2.imread('ronaldo_balon_dor.jpg')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

# calculating object histogram
roihist = cv2.calcHist([hsv],[0, 1], None, [10, 10], [0, 180, 0, 256] )

# normalize histogram and apply backprojection
cv2.normalize(roihist,roihist,0,2,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(dst,-1,disc,dst)

# threshold and binary AND
ret,thresh = cv2.threshold(dst,150,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#0+cv2.THRESH_OTSU
thresh_d = thresh.copy()
thresh = cv2.merge((thresh,thresh,thresh))

# Apply Gaussian Blur
# dst = cv2.GaussianBlur(dst,(5,5),0)
x = cv2.GaussianBlur(thresh,(5,5),0)

res = cv2.bitwise_and(target,x)


# Showing before morph
thresh_c = thresh.copy()
img_c = np.vstack((thresh_c,res))
# img_c = imutils.resize(img_c, height = 700)
cv2.imshow('Before morph', img_c)


# Implementing morphological erosion & dilation
kernel = np.ones((9,9),np.uint8)
thresh = cv2.erode(thresh, kernel, iterations = 1)
thresh = cv2.dilate(thresh, kernel, iterations=1)


# res = np.vstack((target,thresh,res))
res = np.vstack((thresh,res))
#cv2.imwrite('res.jpg',res)
# res = imutils.resize(res, height = 700)
cv2.imshow('After morph', res)
cv2.waitKey(0)

