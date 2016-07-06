#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on June 07, 2016 by 10:10 PM

class Matrix(object):
	"""
	Nothing from the numpy library was used in making this class for inexplicable reasons
	"""
	def __init__(self,rows,cols):
		self.rows = rows
		self.cols = cols
		# self.m = [[0 for x in range(self.cols)] for y in range(self.rows)]
		self.m = self.rows*[self.cols*[0]]
		# self.m = [[0]*self.cols for i in range(self.rows)]
	def display_matrix(self):
		return self.m

	def set_value(self,r,c,value):
		if r< self.rows and c<self.cols:
			self.m[r][c] = value
		else:
			raise ValueError("You're trying to change an element that's not in the matrix. check your r or c values")

mat = Matrix(5,8)
print mat.display_matrix()
mat.set_value(2,3,14)
mat.set_value(4,7,25)
print mat.display_matrix()


