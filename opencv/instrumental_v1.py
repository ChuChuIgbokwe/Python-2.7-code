#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 13, 2016 by 11:46 PM

import numpy as np
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

image = cv2.imread('messi.jpg')
print image.dtype
# img_gray = cv2.imread('messi.jpg',0)
row,col,dim = image.shape
print image.shape
weights = [0.299, 0.587, 0.114]

def weightedAverage(pixel):
    return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]

grey = np.zeros((image.shape[0], image.shape[1]),dtype=np.uint8) # init 2D numpy array
print grey.shape
x, y = [],[]
r,c = 0,0
# get row number
# for rownum in range(len(image)):
#     r+=1
#     for colnum in range(len(image[rownum])):
#         c+=1

cy = 0
cx = 0
# new_image =np.zeros((image.shape[0], image.shape[1]),dtype=np.uint8)
print image.shape
l = []
# new_image = []
# for x,y in np.ndenumerate(image):
#     new_image.append(0.299 * x[0] + 0.587 * x[1] + 0.114 * x[2])
    # print new_image
    # print x[0] * 0.299 + x[1] * 0.587 + x[2] *0.114
# for x in image:
#     print x[0]
# print len(new_image)
print cy,cx

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

# def rgb2gray(rgb):
#
#     r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
#     gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
#
#     return gray

img = cv2.imread('messi_1.jpg')
g = rgb2gray(img)
plt.imshow(g, cmap = plt.get_cmap('gray'))
plt.show()
# cv2.imshow('',g)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
a = np.arange(24).reshape((4,2,3))

    # l.append(0.299 * x[0] + 0.587 * x[1] + 0.114 * x[2])

print l























# import os,sys
# import Image
# jpgfile = Image.open("messi.jpg")
#
# # print jpgfile.bits, jpgfile.size, jpgfile.format
# print jpgfile
