#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 19, 2016 by 3:21 PM

class Point:

	def __init__(self, initX, initY):
		""" Create a new point at the given coordinates. """
		self.x = initX
		self.y = initY

	def getX(self):
		'''
		accessor functiong for x coordinate
		:return:
		'''
		return self.x

	def getY(self):
		'''
		accessor functiong for y coordidante
		:return:
		'''
		return self.y

	def distanceFromOrigin(self):
		return ((self.x ** 2) + (self.y ** 2)) ** 0.5


	def distanceFromPoint(self, target_point):
		'''
		Add a distanceFromPoint method that works similar to distanceFromOrigin except that it takes a Point
		as a parameter and computes the distance between that point and self.
		:param self:
		:param target_point:
		:return:
		'''
		return ((self.x - target_point.x)**2 + (self.y - target_point.y)**2)**0.5

	def reflect_x(self):
		'''
		Add a method reflect_x to Point which returns a new Point, one which is the reflection of the point about
		the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)
		:return:
		'''
		return (self.x, -self.y)

	def slope_from_origin(self):
		'''
		Add a method slope_from_origin which returns the slope of the line joining the origin to the point. For example,
		Point(4, 10).slope_from_origin()
		2.5
		:return:
		'''
		if self.x != 0:
			return self.y/float(self.x)
		else:
			return None

	def get_line_to(self,target_point):
		'''
		Write a method in the Point class so that if a point instance is given another point, it will compute the
		equation of the straight line joining the two points. It must return the two coefficients as a
		tuple of two values
		:param target_point:
		:return:
		'''
		m = (float(target_point.y - self.y))/(target_point.x - self.x)
		c = self.y - m * self.x
		return (m,c)

	def move(self,dx,dy):
		'''
		Add a method called move that will take two parameters, call them dx and dy. The method will cause the point
		to move in the x and y direction the number of units given. (Hint: you will change the values of
		the state of the point)
		:return:
		'''
		self.x += dx
		self.y += dy

	def centre_and_radius(self, point2, point3):
		'''
		Given three points that fall on the circumference of a circle, find the center and radius of the circle
		:param self:
		:param point2:
		:param point3:
		:return:
		'''
		m12 = (float(self.y - point2.y)) / (self.x - point2.x)
		m23 = (float(point3.y - point2.y)) / (point3.x - point2.x)

		x = (m12 * m23 * (point3.y - self.y) + m12*(point2.x + point3.x) - m23*(self.x + point2.x)) / (2 * (m12 - m23))
		y = -(1/m12) * (x - ((self.x + point2.x) / 2.0)) + ((self.y + point2.y) / 2.0)
		# To find the radius, use the distance formula with center and one point.
		r = ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
		return (x,y,r)

	def __str__(self):
		return "x=" + str(self.x) + ", y=" + str(self.y)

	def halfway(self, target):
		mx = (self.x + target.x) / 2
		my = (self.y + target.y) / 2
		return Point(mx, my)

p = Point(5, 5)
q = Point(6, -2)
r = Point(2, -4)
mid = p.halfway(q)

print(mid)
print(mid.getX())
print(mid.getY())


print p.distanceFromPoint(q)
print p.reflect_x()
print p.slope_from_origin()
print p.get_line_to(q)
print p.centre_and_radius(q,r)

p.move(2,2)
print p
