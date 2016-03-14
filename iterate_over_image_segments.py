#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 11, 2016 by 8:52 AM

import cv2
import numpy as np
from copy import copy

'''
The code below does a decent job of isolating individual beetles, or clusters of beetles by using their distinctive
yellow and black stripes and encircles them in red. However, at this point I would like to be able to further analyze
each enclosed red blob to be able to determine how many beetles are in each blob, perhaps by using identifying features
such as the black head or yellow thorax. So the question is, how can I isolate and iterate over the blobs for further
processing?
'''

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#load file
target = cv2.imread('mcb3.jpg')

#convert to hsv and gray for procesing
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)

#Bounds for yellowish colors
lower_y = np.array([18,0,0],dtype=np.uint8)
upper_y = np.array([30,255,255],dtype=np.uint8)

#Make colors in yellowish range black and all others white to find yellow stripes
threshy = 255-cv2.inRange(hsvt, lower_y, upper_y)
cv2.imwrite('threshy.jpg',threshy)

#Make dark colors black and all others white to find dark stripes
ret, threshg = cv2.threshold(gray,30,255,cv2.THRESH_BINARY)
cv2.imwrite('threshg.jpg',threshg)


#merge black and yellow stripes
thresh = copy(threshg)
thresh[threshy == 0] = 0
thresh = 255-thresh
cv2.imwrite('thresh.jpg',thresh)
cv2.imshow('thresh',thresh)

#Blur and threshold to smooth
thresh = cv2.blur(thresh,(30,30))
ret, thresh = cv2.threshold(thresh,100,255,cv2.THRESH_BINARY)
cv2.imwrite('threshbs.jpg',thresh)
cv2.imshow('threshbs',thresh)

#Get edges and draw in red on original image
edges = cv2.Canny(thresh,100,200)
edges[edges != 255] = 0
edges = cv2.dilate(edges, None)
target[edges == 255] = (0, 0, 255)
cv2.imwrite("res.jpg", target)
cv2.imshow('res',target)



