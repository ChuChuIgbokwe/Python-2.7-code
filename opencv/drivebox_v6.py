#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 10, 2017 by 10:56 PM

import numpy as np
import matplotlib.pyplot as plt
import cv2
import math


# Determine the Region of Interest (ROI) by slicing the image (focus the middle part)
# Grayscale the ROI
# Equalized the grayscaled ROI with cv2.equalizeHist
# Apply Gaussian blur to (3)
# Threshold (4) by using cv2.adaptiveThreshold
# Skeletonize (5) by using skimage.morphology.skeletonize
# Apply the cv2.HoughLines on (6)


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

def draw_lines(img, lines, color=(255, 0, 0), thickness=7):
    # TO-DO: refactor and cleanup this function
    right_slope = []
    left_slope = []

    left_lines = []
    right_lines = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            m = ((y1 - y2) / float(x1 - x2))  # slope
            # print(m, i)
            if m <= -0.2:
                left_slope.append(m)
                left_lines.append((x1, y1))
            elif m >= 0.2 and m <= 0.88:
                right_slope.append(m)
                right_lines.append((x2, y2))

    # average left and right slopes
    right_slope = sorted(right_slope)[int(len(right_slope) / 2.0)]
    left_slope = sorted(left_slope)[int(len(left_slope) / 2.0)]

    start_left_y = sorted([line[1] for line in left_lines])[int(len(left_lines) / 2.0)]
    start_left_x = [line[0] for line in left_lines if line[1] == start_left_y][0]

    start_right_y = sorted([line[1] for line in right_lines])[int(len(right_lines) / 2.0)]
    start_right_x = [line[0] for line in right_lines if line[1] == start_right_y][0]

    # next we extend to the car
    end_left_x = int((img.shape[1] - start_left_y) / left_slope) + start_left_x
    end_right_x = int((img.shape[1] - start_right_y) / right_slope) + start_right_x

    cv2.line(img, (start_left_x, start_left_y), (end_left_x, img.shape[1]), color, thickness)
    cv2.line(img, (start_right_x, start_right_y), (end_right_x, img.shape[1]), color, thickness)


def _draw(img, lines):
    """ draw results """
    mainLineX1 = 0
    mainLineY1 = 0
    mainLineX2 = 0
    mainLineY2 = 0
    for line in lines:
        for obj in line:
            [x1, y1, x2, y2] = obj
            mainLineX1 = mainLineX1 + x1
            mainLineY1 = mainLineY1 + y1
            mainLineX2 = mainLineX2 + x2
            mainLineY2 = mainLineY2 + y2
            dx, dy = x2 - x1, y2 - y1
            angle = np.arctan2(dy, dx) * 180 / np.pi
            print np.arctan2(dy, dx)
            if angle <= 20 and angle >= - 20:
                return img
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 7)
    dx, dy = mainLineX2 - mainLineX1, mainLineY1 - mainLineY2
    angle = np.arctan2(dy, dx) * 180 / np.pi
    print angle
    return img


def _debug_draw(edge, lines):
    """ debug with draw """
    print ""

    # img = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    for line in lines:
        # print json.dumps(line)
        for obj in line:
            [x1, y1, x2, y2] = obj
            dx, dy = x2 - x1, y2 - y1
            angle = np.arctan2(dy, dx) * 180 / np.pi

            if angle <= 20 and angle >= - 20:
                return edge
            cv2.line(edge, (x1, y1), (x2, y2), (0, 255, 0), 7)
    return edge



kernel = np.ones((5,5), np.uint8)
# cap = cv2.VideoCapture("street_driving.mp4")
cap = cv2.VideoCapture("drivebox_video.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    height, width, channels = frame.shape
    horizon_height = height/2
    upper_frame_row = height * 3 / 12
    # print horizon_height
    # horizon = height / 2
    # halfWidth = width / 2
    roi = frame.copy()
    roi[0:height/2, :] = (0,0,0)
    # roi_denoised = cv2.fastNlMeansDenoising(roi,None,10,7,21)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray)
    blur = cv2.GaussianBlur(equ, (5,5), 3)

    a_thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    # closing = cv2.morphologyEx(a_thresh, cv2.MORPH_CLOSE, kernel)
    # opening = cv2.morphologyEx(a_thresh, cv2.MORPH_OPEN, kernel)
    # a_thresh = cv2.GaussianBlur(a_thresh, (5, 5), 3)
    ret, thresh = cv2.threshold(blur, 250, 255, cv2.THRESH_BINARY) #cv2.THRESH_TOZERO, THRESH_BINARY,ADAPTIVE_THRESH_MEAN_C
    # a_thresh = cv2.adaptiveThreshold(blur, 128, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)
    edges = cv2.Canny(a_thresh, (0.5* ret), ret, apertureSize=3, L2gradient=True)
    # if len(np.nonzero(edges)[0]) > 30000:
    #     edges = cv2.Canny(thresh, 75, 180, apertureSize=3)
    # # Ignore edges in parts of image by obscuring them
    # rows, cols = edges.shape
    # cv2.rectangle(edges, (0, 0), (cols, int(5 * rows / 8)), (0, 0, 0), -1, 8)
    # cv2.rectangle(edges, (0, 0), (int(cols / 8), rows), (0, 0, 0), -1, 8)
    # cv2.line(edges, (0, 380), (300, 240), (0, 0, 0), 135)

    skel = skeletonize(thresh,(3,3))
    # skel = cv2.GaussianBlur(skel,(5,5),3)


    minLineLength = 100 #height * horizon_height
    maxLineGap = 5 #height * 0.2
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, horizon_height/4, minLineLength=minLineLength, maxLineGap=maxLineGap)
    lines_matl = np.matrix(lines, 'float')
    # slope = np.divide(np.subtract(lines_matl[:, 3], lines_matl[:, 1]), np.subtract(lines_matl[:, 2], lines_matl[:, 0]))
    if lines_matl.size > 1:

        # Calculate slope, hood, and horizon intercept for each line
        slope = np.divide(np.subtract(lines_matl[:, 3], lines_matl[:, 1]),
                          np.subtract(lines_matl[:, 2], lines_matl[:, 0]))

        b = np.subtract(lines_matl[:, 1] + upper_frame_row,
                        np.multiply(slope, (lines_matl[:, 0] + left_line_hood_capture_range[0])))

        hood_col = np.divide(np.subtract(upper_frame_row + height, b), slope)
        horizon_col = np.divide(np.subtract(horizon_row, b), slope)

        # Parse left lines based on hood/horizon intercepts and slope
        left_lines = np.logical_and(hood_col > left_line_hood_range[0], hood_col < left_line_hood_range[1])
        left_lines = np.logical_and(left_lines, horizon_col > horizon_range[0])
        left_lines = np.logical_and(left_lines, horizon_col < horizon_range[1])
        left_lines = np.logical_and(left_lines, slope < 0)

        if any(left_lines):
            # Parse left lines based on max slope then maximum hood intercept
            left_line = np.logical_and(left_lines, hood_col == np.max(hood_col[left_lines]))
            left_line = np.logical_and(left_line, slope == np.min(slope[left_line]))

            # Pull left line hood/horizon intercept and lines_mat index
            left_line_hood = hood_col[left_line]
            left_line_horizon = horizon_col[left_line]
            left_row_idx, left_col_idx = np.where(left_line)

    else:
        left_lines = []

    b = np.subtract(lines_matl[:, 1] + upper_frame_row,
                    np.multiply(slope, (lines_matl[:, 0] + left_line_hood_capture_range[0])))


    if lines is not None:
        for line in lines:
            for obj in line:
                [x1, y1, x2, y2] = obj
        # for x1, y1, x2, y2 in lines[0]:
                angle = np.abs(np.arctan2((y2 - y1), (x2 - x1)) * 180 / np.pi)
                if angle > 17:
                    lenXY = np.sqrt((x1-x2)**2 + (y1-y2)**2)
                    x3 = int(x2 + (x2-x1)/lenXY * 100)
                    y3 = int(y2 + (y2-y1)/lenXY * 100)
                    cv2.line(frame, (x1, y1), (x3, y3 ), (0, 0, 255), 5)
        # # draw_lines(frame, lines)
        # _draw(frame,lines)
        # _debug_draw(frame,lines)
    # print lines[0][0][1]
    # print lines[0][0].dtype
    # cv2.line(frame,(lines[0][0][0],lines[0][0][1]),(lines[0][0][2],lines[0][0][3]),(255,255,255),7)
    cv2.line(frame,(100,100),(400,400),(0,0,0),7)
    cv2.imshow("",frame)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#OTSU's Method
# high_thresh, thresh_im = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# lowThresh = 0.5*high_thresh
