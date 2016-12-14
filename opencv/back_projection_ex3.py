#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 11, 2016 by 8:58 AM

import numpy as np
import cv2

img = cv2.imread('sidewalk_survey.jpg')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
h,w,_ = img.shape
roi_h = 40
roi_w = 200

cv2.rectangle(img,(int(w/2.0 - roi_w/2.0), h - roi_h),(int(w/2.0 + roi_w/2.0), h),(0,0,255),3)
# Convert to hsv
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

roi=img[(h - roi_h):h,(w/2.0 - roi_w/2.0):(w/2.0 + roi_w/2.0)]
roi_hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

# roi_hsv = np.zeros([60,50,3], dtype=hsv.dtype)

# for i in range(1,3,1):
# 	roi_hsv[i*10:i*10+10,0:10] = roi[row[i]:row[i]+10, col[i]:col[i]+10]
y_coords = np.array([h / 2.0 - roi_h / 2.0, h / 2.0 - roi_h / 2.0, h / 2.0 + roi_h / 2.0, h / 2.0 + roi_h / 2.0])
x_coords = np.array([w - roi_w, w,w - roi_w, w])

roi_hist = cv2.calcHist( [roi_hsv], [0, 1], None, [10, 10], [0, 180, 0, 256] )
cv2.normalize(roi_hist,roi_hist,0,1,cv2.NORM_MINMAX)

dst = cv2.calcBackProject([hsv],[0,1],roi_hist,[0,180,0,256],1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(dst,-1,disc,dst)

# threshold and binary AND
ret,thresh = cv2.threshold(dst,127,192,0+cv2.THRESH_OTSU)#0+cv2.THRESH_OTSU
thresh_copy = thresh.copy()
thresh = cv2.merge((thresh,thresh,thresh))

# x = cv2.GaussianBlur(thresh,(5,5),0)
res = cv2.bitwise_xor(img,thresh)

# Apply Gaussian Blur
# dst = cv2.GaussianBlur(dst,(5,5),0)

# Implementing morphological erosion & dilation
# kernel = np.ones((9,9),np.uint8)
# thresh = cv2.erode(thresh, kernel, iterations = 1)
# thresh = cv2.dilate(thresh, kernel, iterations=1)

res = cv2.bitwise_xor(img,thresh)
res = np.vstack((res,thresh))

# Code to draw the contours and fill them in
contours, hierarchy = cv2.findContours(thresh_copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
cv2.drawContours(res, cnts, -1,(0,255,0),2)
cv2.fillPoly(res,contours,(0,0,255))

cv2.imshow('res and thresh', res)
cv2.imshow('img',img)
# cv2.imshow('roi',roi)
cv2.waitKey(0)
# if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#
# cap.release()
# cv2.destroyAllWindows()
#
