#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 10, 2017 by 10:43 PM

import cv2
import numpy as np
import scipy.ndimage.morphology as m

from skimage.morphology import skeletonize
from skimage.viewer import ImageViewer
image = cv2.imread('messi.jpg',0)
img1 = cv2.imread('messi_1.jpg',0)

# print len(img.shape)
# print len(image.shape)
# gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# print len(gray.shape)
# ret,thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
# count_white = cv2.countNonZero(thresh)
# print count_white
# height, width, depth = image.shape

img2 = image.copy()
# img2 =

# L = half of lane width in pixels?
L = 175

# for n in xrange(height):
#     # img2[n] = 2 * img[n] - (img[n-L] + img[n+L]) - abs((img[n-L] - img[n+L]))
#     img2[:, n] = 2 * img[:, n] - (img[:, n - L] + img[:, n + L]) - abs((img[:, n - L] - img[:, n + L]))
#
# cv2.imshow('',img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# kernel = np.ones((1,1),np.uint8)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# blur = cv2.GaussianBlur(opening,(1,1),0)
# ret3,th4 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# th4[th4 == 255] = 1
# skel = skeletonize(th4)
# viewer = ImageViewer(skel)
# viewer.show()

# def skeletonize(img):
#     """ OpenCV function to return a skeletonized version of img, a Mat object"""
#
#     #  hat tip to http://felix.abecassis.me/2011/09/opencv-morphological-skeleton/
#     img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     img = img.copy() # don't clobber original
#     skel = img.copy()
#
#     skel[:,:] = 0
#     kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
#
#     while True:
#         eroded = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)
#         temp = cv2.morphologyEx(eroded, cv2.MORPH_DILATE, kernel)
#         temp  = cv2.subtract(img, temp)
#         skel = cv2.bitwise_or(skel, temp)
#         img[:,:] = eroded[:,:]
#         if cv2.countNonZero(img) == 0:
#             break
#
#     return skel
def skeletonize(img):
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        size = np.size(gray)
        skel = np.zeros(gray.shape, np.uint8)

        ret, img = cv2.threshold(gray, 127, 255, 0)
    else:
        size = np.size(img)
        skel = np.zeros(img.shape, np.uint8)
        ret, img = cv2.threshold(img, 127, 255, 0)

    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    done = False

    while (not done):
        eroded = cv2.erode(img, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(img, temp)
        skel = cv2.bitwise_or(skel, temp)
        img = eroded.copy()

        zeros = size - cv2.countNonZero(img)
        if zeros == size:
            done = True
    return skel

size = np.size(img1)
skel = np.zeros(img1.shape,np.uint8)

ret,img = cv2.threshold(img1,127,255,0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

# img = 255 - img
# img = cv2.dilate(img, element, iterations=3)

done = False

while( not done):
    eroded = cv2.erode(img,element)
    temp = cv2.dilate(eroded,element)
    temp = cv2.subtract(img,temp)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy()

    zeros = size - cv2.countNonZero(img)
    if zeros==size:
        done = True


# def sk(img):
#     h1 = np.array([[0, 0, 0],[0, 1, 0],[1, 1, 1]])
#     m1 = np.array([[1, 1, 1],[0, 0, 0],[0, 0, 0]])
#     h2 = np.array([[0, 0, 0],[1, 1, 0],[0, 1, 0]])
#     m2 = np.array([[0, 1, 1],[0, 0, 1],[0, 0, 0]])
#     hit_list = []
#     miss_list = []
#     for k in range(4):
#         hit_list.append(np.rot90(h1, k))
#         hit_list.append(np.rot90(h2, k))
#         miss_list.append(np.rot90(m1, k))
#         miss_list.append(np.rot90(m2, k))
#     img = img.copy()
#     while True:
#         last = img
#         for hit, miss in zip(hit_list, miss_list):
#             hm = m.binary_hit_or_miss(img, hit, miss)
#             img = np.logical_and(img, np.logical_not(hm))
#         if np.all(img == last):
#             break
#     return img
#
# ret,img2 = cv2.threshold(img1,127,255,0)
# element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# img2 = 255 - img2
# img2 = cv2.dilate(img2, element, iterations=3)
#
# SK = sk(img2)
# m.imshow(SK, cmap="gray", interpolation="nearest")


s = skeletonize(image)
cv2.imshow("skel",s )
cv2.imshow('modified skel',skel)
cv2.imshow('O',img1)
cv2.imshow("original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


