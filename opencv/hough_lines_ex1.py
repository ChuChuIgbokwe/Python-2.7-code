#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 13, 2016 by 9:12 PM

import numpy as np
import cv2
import matplotlib.pyplot as plt


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



img = cv2.imread('openroad.jpg')
print img.dtype
pts1 = np.float32( [[0,img.shape[0]],[0,img.shape[0]/2],[img.shape[1],img.shape[0]],[img.shape[1],img.shape[0]/2]])

# pts1 = np.float32( [[0,img.shape[0]],[0,img.shape[0]/2],[img.shape[1],img.shape[0]],[img.shape[1],img.shape[0]/2]])

# pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
pts2 = np.float32( [[0,0],[img.shape[1],0],[0,img.shape[0]],[img.shape[1],img.shape[0]]] )

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(img.shape[1],img.shape[0]))
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(gray)
blur = cv2.GaussianBlur(equ, (15,15), 0)
ret, thresh = cv2.threshold(blur, 224, 255, cv2.THRESH_BINARY)
# contours,hier = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# cnt = contours[0]
# edges = cv2.Canny(thresh,50,150,apertureSize = 3,L2gradient=True)
edges = cv2.Canny(thresh, (0.5* ret), ret, apertureSize=3, L2gradient=True)
skel = skeletonize(thresh,(3,3))

# if len(np.nonzero(edges)[0]) > 30000:
#     edges = cv2.Canny(thresh, 75, 180, apertureSize=3)
# # Ignore edges in parts of image by obscuring them
# rows, cols = edges.shape
# cv2.rectangle(edges, (0, 0), (cols, int(5 * rows / 8)), (0, 0, 0), -1, 8)
# cv2.rectangle(edges, (0, 0), (int(cols / 8), rows), (0, 0, 0), -1, 8)
# cv2.line(edges, (0, 380), (300, 240), (0, 0, 0), 135)


minLineLength = 150
maxLineGap = 15
lines = cv2.HoughLinesP(skel,1,np.pi/180,50,minLineLength=minLineLength,maxLineGap=maxLineGap)

for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),5)


line_img = np.zeros(img.shape, dtype=np.uint8)

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


draw_lines(img,lines)



# cv2.line(img, tuple(pts1[0]), tuple(pts1[1]), (255,0,0), 7)
# cv2.line(img, tuple(pts1[1]), tuple(pts1[3]), (255,0,0), 7)
# cv2.line(img, tuple(pts1[3]), tuple(pts1[2]), (255,0,0), 7)
# cv2.line(img, tuple(pts1[2]), tuple(pts1[0]), (255,0,0), 7)
#
# plt.imshow(pts2)
# plt.show()

# contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img,contours,-1,(0,255,0),7)

# Code to draw the contours and fill them in
# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img,contours,-1,(0,255,0),-1)

# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnts = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
# cv2.drawContours(img, cnts, -1,(0,255,0),2)
# cv2.fillPoly(img,contours,(100,200,100))
# cv2.imwrite('houghlines5.jpg',img)

# cv2.imwrite('houghlines1.jpg',img)
cv2.imshow('transformed image',img)
# cv2.imshow('blurred',blur)
# cv2.imshow('equalized hsv',hsv)
# cv2.imshow('skel',skel)
# cv2.imshow('original',img)
# cv2.imshow('thresh',thresh)
# cv2.imshow('edges',edges)
# cv2.imshow('output',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.waitKey(0)
cv2.destroyAllWindows()