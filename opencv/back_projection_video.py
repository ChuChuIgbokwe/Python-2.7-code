#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 08, 2016 by 1:24 AM

import numpy as np
import cv2
#
# def main()
cap = cv2.VideoCapture('walking_down_the_sidewalk.mp4')

# take first frame of the video
ret,frame = cap.read()
# setup initial location of window
r,h,c,w = 50,90,110,125 # simply hardcoded the values
track_window = (c,r,w,h)
# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]
hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])


#Read the first frame of the video
# ret,frame = cap.read()
while(cap.isOpened()):
    ret, frame = cap.read()
    w,h,_ = frame.shape
    width  = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    print w,h
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # roi_hist = cv2.calcHist([hsv_roi],[0, 1], None, [10, 10], [0, 180, 0, 256] )
    # cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    # print frame.shape
    cv2.rectangle(frame,(220,250),(260,270),(0,255,0),3)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# cap = cv2.VideoCapture('slow_traffic_small.mp4')

# def run_main():
#     cap = cv2.VideoCapture('slow_traffic_small.mp4')
#     # Read the first frame of the video
#     ret, frame = cap.read()
#     # Set the ROI (Region of Interest). Actually, this is a
#     # rectangle of the building that we're tracking
#     c,r,w,h = 900,650,70,70
#     track_window = (c,r,w,h)
#     # Create mask and normalized histogram
#     roi = frame[r:r+h, c:c+w]
#     hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#
#     lower = np.array([0., 30.,32.],dtype=np.uint8)
#     upper = np.array([180., 255.,255.],dtype=np.uint8)
#
#     mask = cv2.inRange(hsv_roi,lower, upper)
#     roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
#     cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
#     term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 80, 1)
#
#     while True:
#         ret, frame = cap.read()
#         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
#         ret, track_window = cv2.meanShift(dst, track_window, term_crit)
#         x,y,w,h = track_window
#         cv2.rectangle(frame, (x,y), (x+w,y+h), 255, 2)
#         cv2.putText(frame, 'Tracked', (x-25,y-10), cv2.FONT_HERSHEY_SIMPLEX,
#             1, (255,255,255), 2, cv2.CV_AA)
#
#         cv2.imshow('Tracking', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()
# if __name__ == "__main__":
#     run_main()