#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 08, 2016 by 3:39 AM

import numpy as np
import cv2

cap = cv2.VideoCapture('walking_down_the_sidewalk.mp4')
# take first frame of the video
ret,frame = cap.read()

# # set up the ROI for tracking

h,w,_ = frame.shape


hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(hsv_roi, np.array((105., 105., 105.)), np.array((169., 169., 169.)))
# mask = cv2.inRange(hsv_roi, np.array((0., 0., 150)), np.array((0., 0., 180)))
# mask_roi = mask[400:480,85:185]
roi_h = 30
roi_w = 30
row = np.array([85,185])
col = np.array([200,280])

# roi = frame[(h / 2.0 - roi_h / 2.0):(h / 2.0 + roi_h / 2.0), (w - roi_w):w]
# roi = frame[5:15,20:25]
roi=frame[(h - roi_h):h,(w/2.0 - roi_w/2.0):(w/2.0 + roi_w/2.0)]
# roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# print roi_hsv.shape
# roi_hsv = np.zeros([90,10,3], dtype=hsv_roi.dtype)
# for i in xrange(2):
# 	roi_hsv[i*10:i*10+10,0:10] = hsv_roi[row[i]:row[i]+10, col[i]:col[i]+10]
# 	# print roi_hsv

# lower_grey = np.array([0, 25, 0], dtype=np.uint8)
# upper_grey = np.array([180, 255, 255], dtype=np.uint8)
#
lower_grey = np.array([128, 128, 128], dtype=np.uint8)
upper_grey = np.array([192, 192, 192], dtype=np.uint8)
# mask = cv2.inRange(roi, lower_grey, upper_grey)

roi_hist = cv2.calcHist( [roi], [0, 1], None, [9, 5], [0, 180, 0, 256] )
# roi_norm = \
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
frame_counter = 0
# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
while(cap.isOpened()):
	# Take each frame
	ret, frame = cap.read()
	frame_counter += 1
	if frame_counter == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
		frame_counter = 0
		cap = cv2.VideoCapture('walking_down_the_sidewalk.mp4')
	# cv.Flip(frame, flipMode=-1)
	# frame = cv2.flip(frame,0)
	# cv2.rectangle(frame,(85,400),(185,480),(0,0,255),3)
	cv2.rectangle(frame,(int(w/2.0 - roi_w/2.0), h - roi_h),(int(w/2.0 + roi_w/2.0), h),(0,0,255),3)
	frame_b = frame
	# frame_b = cv2.rectangle(frame_b,(220,250),(260,270),(0,255,0),3)
	# h,w,_ = frame.shape

	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_grey, upper_grey)
	# roi=frame[(h - roi_h):h,(w/2.0 - roi_w/2.0):(w/2.0 + roi_w/2.0)]
	# roi_hist = cv2.calcHist( [roi], [0, 1], None, [9, 5], [0, 180, 0, 256] )
	# cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

	dst = cv2.calcBackProject([hsv],[0,1],roi_hist,[0,180,0,256],1)

	# Now convolute with circular disc
	disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))
	cv2.filter2D(dst,-1,disc,dst)
	# cv2.imshow('dst',dst)
	# threshold and binary XOR
	ret,thresh = cv2.threshold(dst,128,192,0+cv2.THRESH_OTSU)
	thresh_copy = thresh.copy()

	# Implementing morphological erosion & dilation
	# kernel = np.ones((9,9),np.uint8)
	# thresh = cv2.erode(thresh, kernel, iterations = 1)
	# thresh = cv2.dilate(thresh, kernel, iterations=1)

	thresh = cv2.merge((thresh,thresh,thresh))

	# Apply Gaussian Blur
	x = cv2.GaussianBlur(thresh,(5,5),0)

	res = cv2.bitwise_xor(frame,thresh)#, mask=thresh_copy

	# Code to draw the contours and fill them in
	contours, hierarchy = cv2.findContours(thresh_copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cnts = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
	cv2.drawContours(res, cnts, -1,(0,255,0),2)
	cv2.fillPoly(res,contours,(255,0,0))

	cv2.imshow('frame',res)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

