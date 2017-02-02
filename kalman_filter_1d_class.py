#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 28, 2017 by 10:59 PM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys

class KalmanFilter1D:
    def __init__(self, x0, R, Q,P):
        self.x = x0 #initial state
        self.R = R #sensor noise/ variance
        self.Q = Q # movement noise
        self.P = P # initial variance

    def update(self,z):
        self.x = (self.P * z + self.x * self.R) / (self.P + self.R) #corresponds to gaussian multiplication
        self.P = 1 / (1 / self.P + 1 / self.R)

    def predict(self, u=0.0):
        self.x += u #corresponds to gaussian addition
        self.P += self.Q