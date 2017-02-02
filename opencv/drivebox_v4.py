#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 19, 2016 by 7:21 PM

import numpy as np
import cv2

# class LaneDeteector(object):
#     def __init__(self,video,prob_hough=True):
#         self.video = video
#         self.cap = cv2.VideoCapture(self.video)
#         self.height = self.cap

kernel = np.ones((5,5), np.uint8)
cap = cv2.VideoCapture("street_driving.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    height, width, channels = frame.shape
    horizon = height / 2
    halfWidth = width / 2
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.fastNlMeansDenoising(gray,None,10,7,21)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    gray = cv2.equalizeHist(gray)
    blur_gray = cv2.GaussianBlur(gray, (5,5), 0)
    roi = gray[horizon:height, 0:width]
    edges = cv2.Canny(roi, 1, 200, apertureSize=3,L2gradient=True)
    # edges = cv2.adaptiveThreshold(edges,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,41,-3)
    vertical = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("",edges)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


