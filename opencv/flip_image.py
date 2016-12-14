#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 02, 2016 by 10:34 PM

'''
Not working
'''
import numpy as np
import cv2
import copy

img=cv2.imread('ronaldo.png')
rimg=img.copy()
fimg=img.copy()
rimg=cv2.flip(img,1)
fimg=cv2.flip(img,0)
cv2.imshow("Original", img)
cv2.imshow("vertical flip", rimg)
cv2.imshow("horizontal flip", fimg)
cv2.waitKey(0)
cv2.destroyAllWindows()




