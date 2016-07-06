#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 23, 2016 by 4:56 PM

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


class Rectangle:
	'''
	 Create a class definition for a Rectangle class using this idea. To create a Rectangle object at location
	 (4,5) with width 6 and height 5, we would do the following:
	 r = Rectangle(Point(4, 5), 6, 5)
	'''
	def __init__(self,location,width,height):
		self.location = location
		self.width = width
		self.height = height

	def getwidth(self):
		return self.width

	def getheight(self):
		return self.height

	def __str__(self):
		return "location: " + str(self.location) + ", width=" + str(self.width) + ", height=" + str(self.height)

	def area(self):
		return self.width * self.height

	def perimeter(self):
		return 2*self.width + 2*self.height

	def transpose(self):
		'''
		method in the Rectangle class that swaps the width and the height of any rectangle instance
		:return:
		'''
		self.width,self.height = self.height,self.width

	def contains(self, item):
		if item.x < 0 and item.x < self.location.x:
			return False
		elif item.y < 0 and item.y < self.location.x:
			return False
		else:
			width_limit = self.width + self.location.x
			height_limit = self.height + self.location.y
			if item.x < width_limit and item.y < height_limit:
				return True
			else:
				return False

loc = Point(4, 5)
r = Rectangle(loc, 6, 5)
print r
print r.area()
print r.perimeter()
r.transpose()
print r
print ''

l = Rectangle(Point(0, 0), 10, 5)

print l.contains(Point(0, 0))
print l.contains(Point(3, 3))
print l.contains(Point(3, 7))
print l.contains(Point(3, 5))
print l.contains(Point(3, 4.99999))
print l.contains(Point(-3, -3))