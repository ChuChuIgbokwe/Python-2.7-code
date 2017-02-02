#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 18, 2016 by 1:11 PM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys

img = cv2.imread("sheet_music.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_inv = cv2.bitwise_not(gray)

# Apply adaptiveThreshold at the bitwise_not of gray
a_thresh = cv2.adaptiveThreshold(gray_inv, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,-2)

# Create the images that will use to extract the horizontal and vertical lines
vertical = a_thresh.copy()
horizontal = a_thresh.copy()

# Specify size on horizontal axis
horizontal_cols = horizontal.shape[1]/30

# Create structure element for extracting horizontal lines through morphology operations
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT,(horizontal_cols,1))

# Apply morphology operations Erosion followed by dilation is called opening
horizontal = cv2.morphologyEx(horizontal,cv2.MORPH_OPEN,horizontalStructure)

# Specify size on vertical axis
vertical_rows = vertical.shape[0]/30

# Create structure element for extracting vertical lines through morphology operations
verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT,(1,vertical_rows))

# Apply morphology operations Erosion followed by dilation is called opening
vertical = cv2.morphologyEx(vertical,cv2.MORPH_OPEN,verticalStructure)

#invert vertical image
vertical_inv = cv2.bitwise_not(vertical)

# Extract edges and smooth image according to the logic
#     1. extract edges
#     2. dilate(edges)
#     3. src.copyTo(smooth)
#     4. blur smooth img
#     5. smooth.copyTo(src, edges)

#Step 1
vertical_edges = cv2.adaptiveThreshold(vertical_inv, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,-2)

#Step 2
kernel = np.ones((2,2),dtype=np.uint8)
vertical_edges = cv2.dilate(vertical_edges,kernel)

#Step 3
smooth= vertical_edges.copy()

#Step 4
smooth = cv2.blur(smooth,(2,2))

#Step 5

final = cv2.bitwise_or(vertical_inv,smooth)

cv2.imshow('final image',final)
cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()