#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 11, 2017 by 12:28 PM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys


def __find_from_to_xy(img, obj, cfg):
    """ find from pp (x,y) and to pp (x,y) """
    ht, wd, dp = img.shape
    [rho, theta] = obj

    a, b = np.cos(theta), np.sin(theta)
    x0, y0 = a * rho, b * rho

    # y = ax + b
    x1, y1 = int(x0 + 1000 * (-b)), int(y0 + 1000 * (a))
    x2, y2 = int(y0 - 1000 * (-b)), int(y0 - 1000 * (a))

    # boundary check
    x1 = x1 if x1 <= wd else x1 if x1 >= 0 else 0
    x2 = x2 if x2 <= wd else x2 if x2 >= 0 else 0
    y1 = y1 if y1 <= ht else y1 if y1 >= int(ht / 2) else int(ht / 2)
    y2 = y2 if y2 <= ht else ht if y2 >= int(ht / 2) else int(ht / 2)
    return x1, y1, x2, y2


def __find_angle(img, obj, cfg):
    """ angle """
    x1, y1, x2, y2 = __find_from_to_xy(img, obj, cfg)
    dx, dy = x2 - x1, y2 - y1
    angle = np.arctan2(dy, dx) * cfg['filter']['invtheta']
    return angle, x1, y1, x2, y2


def _draw(img, lines, cfg):
    """ draw results """
    for line in lines:
        for obj in line:
            angle, x1, y1, x2, y2 = __find_angle(img, obj, cfg)
            if angle <= cfg['filter']['angle'] and angle >= - cfg['filter']['angle']:
                return img
            cv2.line(img, (x1, y1), (x2, y2), cfg['color']['blue'], 2)
    return img






def skeletonize(image, size, structuring=cv2.MORPH_RECT):
    # determine the area (i.e. total number of pixels in the image),
    # initialize the output skeletonized image, and construct the
    # morphological structuring element
    area = image.shape[0] * image.shape[1]
    skeleton = np.zeros(image.shape, dtype="uint8")
    elem = cv2.getStructuringElement(structuring, size)

    # keep looping until the erosions remove all pixels from the
    # image
    while True:
        # erode and dilate the image using the structuring element
        eroded = cv2.erode(image, elem)
        temp = cv2.dilate(eroded, elem)

        # subtract the temporary image from the original, eroded
        # image, then take the bitwise 'or' between the skeleton
        # and the temporary image
        temp = cv2.subtract(image, temp)
        skeleton = cv2.bitwise_or(skeleton, temp)
        image = eroded.copy()

        # if there are no more 'white' pixels in the image, then
        # break from the loop
        if area == area - cv2.countNonZero(image):
            break

    # return the skeletonized image
    return skeleton

img = cv2.imread('openroad.jpg',0)

equ = cv2.equalizeHist(img)
blur = cv2.GaussianBlur(equ, (5,5), 0)
ret, thresh = cv2.threshold(blur, 224, 255, cv2.THRESH_BINARY)
contours, hier = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contour_lines = [cv2.fitLine(cnt, cv2.cv.CV_DIST_L2, 0, 0.01, 0.01) for cnt in contours]





s = skeletonize(blur,size=(3,3))
ss= skeletonize(thresh,size=(3,3))
edges = cv2.Canny(thresh,50,150,apertureSize = 3)
minLineLength = 150
maxLineGap = 25
lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength,maxLineGap)
print lines
# print lines
# for x1,y1,x2,y2 in lines[0]:
#     cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
#
for line in lines:
    for obj in line:
        [x1, y1, x2, y2] = obj
        dx, dy = x2 - x1, y2 - y1
        angle = np.arctan2(dy, dx) * 180 / np.pi
        if angle <= 20 and angle >= - 20:
            # return img
            cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 2)

cv2.imwrite('lanes.jpg',img)

cv2.imshow('skeleton blur',s)
cv2.imshow('skeleton thresh',ss)
cv2.imshow('original', img)
cv2.imshow('equalised histogram',equ)
# cv2.imshow('blurred',blur)
cv2.imshow('threshold',thresh)
cv2.imshow('edges',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
