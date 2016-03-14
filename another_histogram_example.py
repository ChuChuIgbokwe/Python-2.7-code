#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 04, 2016 by 1:50 PM

import numpy as np
import matplotlib.pyplot as plt
import cv2


gray_img = cv2.imread('ronaldinho.jpg', 1)
cv2.imshow('Ronaldinho',gray_img)
hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
hist2 = cv2.calcHist([gray_img],[0,1],None,[10,10],[0,180, 0, 256])

# fig = plt.figure()
# ax = fig.add_subplot(131)
plt.hist(gray_img.ravel(),256,[0,256])
plt.plot(hist.flatten())
# plt.hist2d()
plt.title('Histogram for gray scale picture')
plt.show()
# plt.hist2d()
while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 27: break             # ESC key to exit
cv2.destroyAllWindows()





# plot a 2D color histogram for green and blue
# ax = fig.add_subplot(131)
# hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None,
# 	[32, 32], [0, 256, 0, 256])
# p = ax.imshow(hist, interpolation = "nearest")
# ax.set_title("2D Color Histogram for Green and Blue")
