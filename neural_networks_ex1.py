#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 21, 2016 by 11:43 AM

import numpy as np
class Neural_Network(object):
	def __init__(self):
		'''
		Define HyperParameters
		:return:
		'''
		self.inputLayerSize = 2
		self.outputLayerSize = 1
		self.hiddenLayerSize = 3
		# Weights
		self.W1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
		self.W2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)

	def sigmoid(self,z):
		'''
		:param z:
		:return: 1/(1 + np.exp(-z))
		'''
		return 1/(1 + np.exp(-z))

	def sigmoid_prime(self,z):
		return np.exp(-z)/((1+np.exp(-z))**2)

	def forward(self,X):
		'''
		Propagete inputs through network
		:param x:
		:return:yHat
		'''
		self.z2 = np.dot(X, self.W1)
		self.a2 = self.sigmoid(self.z2)
		self.z3 = np.dot(self.a2, self.W2)
		yHat = self.sigmoid(self.z3)
		return yHat

X = np.array([[3,5],[5,1],[10,2]])
# X = np.array([[3,5],[5,1],[10,2],[8,3]])
# print X
NN= Neural_Network()
yHat = NN.forward(X)
print yHat
