#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 02, 2016 by 9:10 PM

# cspace.py
import cv2
import numpy as np

# cap = cv2.VideoCapture('BlueUmbrella.webm')
cap = cv2.VideoCapture('walking_down_the_sidewalk.mp4')
def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('h', 'result',0,179,nothing)
cv2.createTrackbar('s', 'result',0,255,nothing)
cv2.createTrackbar('v', 'result',0,255,nothing)

frame_counter = 0

while(1):

    # Take each frame
    _, frame = cap.read()

    frame_counter += 1
    #If the last frame is reached, reset the capture and the frame_counter
    # if frame_counter == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
    #     frame_counter = 0 #Or whatever as long as it is the same as next line
    #     cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, 0)

    if frame_counter == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
        frame_counter = 0
        cap = cv2.VideoCapture('walking_down_the_sidewalk.mp4')

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    # lower_blue = np.array([110,50,50])
    # upper_blue = np.array([130,255,255])

    # lower_grey = np.array([103, 150, 127], dtype=np.uint8)
    # upper_grey = np.array([191, 255, 191], dtype=np.uint8)
    # mask = cv2.inRange(hsv, lower_grey, upper_grey)
    #
    # get info from track bar and appy to result
    h = cv2.getTrackbarPos('h','result')
    s = cv2.getTrackbarPos('s','result')
    v = cv2.getTrackbarPos('v','result')

    # Threshold the HSV image to get only blue colors
    # mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Normal masking algorithm
    lower_blue = np.array([h,s,v])
    upper_blue = np.array([180,255,255])


    mask = cv2.inRange(hsv,lower_blue, upper_blue)


    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()



