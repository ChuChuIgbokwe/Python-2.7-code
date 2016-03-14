#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 04, 2016 by 2:21 PM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys
import colorsys


img = cv2.imread('ronaldinho.jpg',1)
gray_img = cv2.imread('ronaldinho', 0)

# print np.shape(img)
# print 'gray_img shape ', np.shape(gray_img)
hsv_img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
# print 'hist_img shape ',np.shape(hsv_img)
# colorsys.rgb_to_hsv(img[0],img[1],img[2])
#
# cv2.imshow('ronaldinho black and white', hsv_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# roihist = cv2.calcHist([hsv], [0, 1], None, [10, 10], [0, 180, 0, 256])

# grab the image channels, initialize the tuple of colors,
# the figure and the flattened feature vector
chans = cv2.split(img)
colors = ("b", "g", "r")
# plt.figure()
# plt.title("'Flattened' Color Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
features = []

# # loop over the image channels
# # for (chan, color) in zip(chans, colors):
# # 	# create a histogram for the current channel and
# # 	# concatenate the resulting histograms for each
# # 	# channel
# # 	hist = cv2.calcHist([img], [0,1], None, [32,32], [0, 256,0,256])
# # 	features.extend(hist)
# #
# # 	# plot the histogram
# # 	plt.plot(hist, color = color)
# # 	plt.xlim([0, 256])
#
# hist = cv2.calcHist([img], [0,1], None, [32,32], [0, 256,0,256])
# plt.plot(hist)
# plt.plot(hist.flatten)
# plt.xlim([0, 256])
# # here we are simply showing the dimensionality of the
# # flattened color histogram 256 bins for each channel
# # x 3 channels = 768 total values -- in practice, we would
# # normally not use 256 bins for each channel, a choice
# # between 32-96 bins are normally used, but this tends
# # to be application dependent
# plt.show()
# print "flattened feature vector size: %d" % (np.array(features).flatten().shape)


# let's move on to 2D histograms -- I am reducing the
# number of bins in the histogram from 256 to 32 so we
# can better visualize the results
fig = plt.figure()
fig2 = plt.figure()


# plot a 2D color histogram for green and blue
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None,
	[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for Green and Blue")
# plt.colorbar(p)

# plot a 2D color histogram for green and red
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None,
	[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for Green and Red")
# plt.colorbar(p)

# plot a 2D color histogram for blue and red
ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None,
	[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for Blue and Red")
# plt.colorbar(p2)

# plot a 2D color histogram for all
ax2 = fig2.add_subplot(121)
hist = cv2.calcHist([img], [0, 1], None,
	[32, 32], [0, 256, 0, 256])
p2 = ax2.imshow(hist, interpolation = "nearest")
ax2.set_title("2D Color Histogram for All")
# plt.colorbar(p2)


# plot a 2D color histogram for all hsv image
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
ax2 = fig2.add_subplot(122)
hist = cv2.calcHist([hsv_img], [0, 1], None,
	[10,10], [0, 180, 0, 256])
p2 = ax2.imshow(hist, interpolation = "nearest")
ax2.set_title("2D Color Histogram for All HSV ")
# plt.colorbar(p2)


# finally, let's examine the dimensionality of one of
# the 2D histograms
print "2D histogram shape: %s, with %d values" % (
	hist.shape, hist.flatten().shape[0])
plt.show()