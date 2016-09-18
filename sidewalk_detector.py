#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 02, 2016 by 2:42 PM

import numpy as np
import cv2
import rospy
import rosbag
import roslib
#
import sys

from std_msgs.msg import String
from sensor_msgs.msg import Image, PointCloud2
from cv_bridge import CvBridge, CvBridgeError

class SidewalkDetector():
	def __init__(self):

		# Publishers
		self.image_pub = rospy.Publisher('/sidewalk_detector/color/image_raw',Image, queue_size=10)
		self.points_in_pub = rospy.Publisher('/sidewalk_detector/depth/points_in',PointCloud2, queue_size=10)
		self.points_out_pub = rospy.Publisher('/sidewalk_detector/depth/points_out',PointCloud2, queue_size=10)

		# Create the cv_bridge object
		self.bridge = CvBridge()


	def get_roi(self,cv_image):
		'''
		Get the ROI, a 200 x 80 rectangle at the bottom of the video frame
		'''
		# Get the video dimensions
		self.h,self.w,self._ = cv_image.shape
		self.roi_w = 50
		self.roi_h = 50

		# Get 50 x 50 Region of Interest Frame
		self.roi = cv_image[(self.h - self.roi_h):(self.h), (self.w/2.0 - self.roi_w/2.0):(self.w/2.0 + self.roi_w/2.0)]

		# Convert to HSV
		# self.roi_hsv = cv2.cvtColor(self.roi, cv2.COLOR_BGR2HSV)

		# Calculate Histogram and Normalize
		self.roi_hist = cv2.calcHist( [self.roi], [0, 1], None, [10, 10], [0, 180, 0, 256] )
		self.roi_norm = cv2.normalize(self.roi_hist,self.roi_hist,0,1,cv2.NORM_MINMAX)
		return self.roi_norm


	def callback(self,data):
		try:
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		except CvBridgeError as e:
			print(e)

		# Flip image
		cv_image = cv2.flip(cv_image,0)

		# Draw a rectangle around ROI
		cv2.rectangle(cv_image,(int(self.w/2.0 - self.roi_w/2.0), self.h - self.roi_h),(int(self.w/2.0 + self.roi_w/2.0), self.h),(0,0,255),3)

		# Make Image copy
		self.image = cv_image

		# Get the ROI from the first frame
		self.roi_norm = self.get_roi(cv_image)

		# Convert to HSV
		self.hsv_roi = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

		# Calculate Histogram and Normalize
		self.hist = cv2.calcHist( [self.hsv_roi], [0, 1], None, [8, 8], [0, 180, 0, 256] )
		self.hist_norm = cv2.normalize(self.hist,self.hist,0,1,cv2.NORM_MINMAX)

		# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
		self.term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

		self.dst = cv2.calcBackProject([self.hsv_roi],[0,1],self.roi_norm,[0,180,0,256],1)

		# Now convolute with circular disc
		self.disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
		cv2.filter2D(self.dst,-1,self.disc,self.dst)

		# threshold and binary AND
		self.ret,self.thresh = cv2.threshold(self.dst,50,255,cv2.THRESH_TRUNC)
		self.thresh_copy = self.thresh.copy()

			# Implementing morphological erosion & dilation
		self.kernel = np.ones((9,9),np.uint8)
		self.thresh = cv2.erode(self.thresh, self.kernel, iterations = 1)
		self.thresh = cv2.dilate(self.thresh, self.kernel, iterations=1)

		self.thresh = cv2.merge((self.thresh,self.thresh,self.thresh))

		# Apply Gaussian Blur
		self.roi_norm = cv2.GaussianBlur(self.dst,(5,5),0)

		self.res = cv2.bitwise_xor(self.image,self.thresh)

		# Code to draw the contours and fill them in
		self.contours, self.hierarchy = cv2.findContours(self.thresh_copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		self.cnts = sorted(self.contours, key = cv2.contourArea, reverse = True)[:5]
		cv2.drawContours(self.res, self.cnts, -1,(0,255,0),2)
		cv2.fillPoly(self.res,self.contours,(100,200,100))

		cv2.imshow('frame',self.res)
		cv2.waitKey(3)
		# if cv2.waitKey(1) & 0xFF == ord('q'):
		#     break


		try:
			self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
		except CvBridgeError as e:
			print(e)

		rospy.loginfo('callback triggered')


def main(args):
	sidewalk_detector = SidewalkDetector()
	rospy.Subscriber('camera/color/image_raw', Image, sidewalk_detector.callback)
	rospy.init_node('sidewalk_detector', anonymous=True)

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)




# def main():
#
# 	#instantiate class here
# 	while not rospy.is_shutdown():
# 		rospy.spin()
#
# if __name__ == '__main__':
# 	main()
# try:
#
# rospy.spin()
#
# except KeyboardInterrupt:
#
# print("Shutting down")
#
# cv2.destroyAllWindows()
# set video resolution to 320 x 240
#  ret = cap.set(CV_CAP_PROP_FRAME_WIDTH,320);
#  ret = cap.set(CV_CAP_PROP_FRAME_HEIGHT,240);
