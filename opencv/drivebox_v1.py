#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 13, 2016 by 10:45 PM

import numpy as np
import cv2
import math
#
# class LaneDetector():
#
cap = cv2.VideoCapture("street_driving.mp4")
kernel = np.ones((5,5),np.uint8)
#
while cap.isOpened():
    ret, frame = cap.read()
    # print frame.shape
    height, width, channels = frame.shape
    halfHeight = height / 2
    halfWidth = width / 2
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    roi = gray[halfHeight:height, 0:width]

    # gaussian smooth over standard deviation, reduce noise
    gray = cv2.GaussianBlur(roi, (5, 5), 3)
    # smooth and canny edge detection
    edges = cv2.Canny(roi, 1, 200, apertureSize=3,L2gradient=True)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=50, maxLineGap=30)

#     for x1, y1, x2, y2 in lines[0]:
#         angle = math.fabs(math.atan2((y2 - y1), (x2 - x1)) * 180 / np.pi)
#         if angle > 10:
#             cv2.line(frame, (x1, y1 + halfHeight), (x2, y2 + halfHeight), (0, 255, 255, .5), 2)
# # #
#     cv2.imshow('window-name', frame)
    # out.write(frame)

    if cv2.waitKey(33) & 0xFF == ord('q'):
        break
#
cap.release()
# out.release()
cv2.destroyAllWindows()

# class LaneDetector():
#     def __init__(self,videopath):
#         self.video = videopath
#         self.cap = cv2.VideoCapture(self.video)
#         self.original_video = self.cap
#         self.preprocessed_image = None
#
#
#     def __preprocessing(self):
#         grey = cv2.cv
#
#
# cap = cv2.VideoCapture("street_driving.mp4")
# # take first frame of the video
# ret,frame = cap.read()
# #
# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     edges = cv2.Canny(gray, 50, 150, apertureSize=3)
#     lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
#
#     # print lines[0]
#     for rho, theta in lines[0]:
#         a = np.cos(theta)
#         b = np.sin(theta)
#         x0 = a * rho
#         y0 = b * rho
#         x1 = int(x0 + 1000 * (-b))
#         y1 = int(y0 + 1000 * (a))
#         x2 = int(x0 - 1000 * (-b))
#         y2 = int(y0 - 1000 * (a))
#
#         cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
#
#     # cv2.imwrite('houghlines1.jpg',img)
#     cv2.imshow('transformed image', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#
# # # take first frame of the video
# # ret,frame = cap.read()
# #
# # while True:
# #     ret, frame = cap.read()
# #
# #     # Our operations on the frame come here
# #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# #     edges = cv2.Canny(gray,50,150,apertureSize = 3)
# #     # Display the resulting frame
# #     cv2.imshow('original',ret)
# #     # cv2.imshow('frame', hsv)
# #     # cv2.imshow('edges',edges)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
# #
# # # When everything done, release the capture
# # cap.release()
# # cv2.destroyAllWindows()
#
#
# # fourcc = cv2.cv.CV_FOURCC('a', 'v', 'c', '1')
# # out = cv2.VideoWriter('output.mp4', fourcc, 29, (1920, 1080))