#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 02, 2016 by 9:42 PM

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 02, 2016 by 2:42 PM

import numpy as np
import cv2
import rospy
import rosbag
import roslib
import colorsys
import copy
 roslib.load_manifest('sidewalk_detector')

from std_msgs.msg import String
from sensor_msgs.msg import Image, PointCloud2
from cv_bridge import CvBridge, CvBridgeError
from math import floor


#Publishers
image_pub = rospy.Publisher('/sidewalk_detector/color/image_raw',Image, queue_size=10)
points_in_pub = rospy.Publisher('/sidewalk_detector/depth/points_in',PointCloud2, queue_size=10)
points_out_pub = rospy.Publisher('/sidewalk_detector/depth/points_out',PointCloud2, queue_size=10)

#Subscriber
image_sub = rospy.Subscriber('camera/color/image_raw',Image,callback)

#CvBridge
bridge = CvBridge()

#Sidewalk Histogram
sidewalk_histogram = []
#Threshold to determine if a pixel is on the sidewalk or not
sidewalk_threshold = 0.8

def image_processing(self):
	cap = cv2.VideoCapture.read()
	# take first frame of the video
	ret,frame = cap.read()
	w,h,self._ = frame.shape
	w_w = 200
	w_h = 80
	# img_part = img[(w/2.0 - w_w/2.0):(w/2.0 + w_w/2.0),(h - w_h):h]
	roi = frame[(h/2.0 - w_h/2.0):(h/2.0 + w_h/2.0),(w - w_w):w]

	# Convert to HSV
	roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
	hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Calculate Histogram and Normalize
	roi_hist = cv2.calcHist( [roi_hsv], [0, 1], None, [8, 8], [0, 180, 0, 256] )
	roi_norm = cv2.normalize(roi_hist,roi_hist,0,1,cv2.NORM_MINMAX)

	hist = cv2.calcHist( [hsv_roi], [0, 1], None, [8, 8], [0, 180, 0, 256] )
	hist_norm = cv2.normalize(hist,hist,0,1,cv2.NORM_MINMAX)

	# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
	term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

	while(cap.isOpened()):
		# Take each frame
		ret, frame = cap.read()
		frame_b = frame
		h,w,_ = frame.shape

		# Convert BGR to HSV
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		dst = cv2.calcBackProject([hsv],[0,1],roi_hist,[0,180,0,256],1)

		# Now convolute with circular disc
		disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
		cv2.filter2D(dst,-1,disc,dst)

		# threshold and binary AND
		ret,thresh = cv2.threshold(dst,50,255,0+cv2.THRESH_OTSU)
		thresh_d = thresh.copy()

		# Implementing morphological erosion & dilation
		kernel = np.ones((9,9),np.uint8)
		thresh = cv2.erode(thresh, kernel, iterations = 1)
		thresh = cv2.dilate(thresh, kernel, iterations=1)

		thresh = cv2.merge((thresh,thresh,thresh))

		# Apply Gaussian Blur
		dst = cv2.GaussianBlur(dst,(5,5),0)

		res = cv2.bitwise_and(frame_b,thresh)

		# Code to draw the contours and fill them in
		contours, hierarchy = cv2.findContours(thresh_d,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		cnts = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
		cv2.drawContours(res, cnts, -1,(0,255,0),2)
		cv2.fillPoly(res,contours,(100,200,100))

		cv2.imshow('frame',res)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()

def callback(self,data):
	try:
		cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
	except CvBridgeError as e:
		print(e)

	#Code goes Here




	try:
		self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
	except CvBridgeError as e:
		print(e)


	def main():
		rospy.init_node('sidewalk_detector')
		while not rospy.is_shutdown():
			rospy.spin()

	if __name__ == '__main__':
		main()

