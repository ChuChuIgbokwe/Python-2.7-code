#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 29, 2017 by 3:47 AM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.linalg as linalg

import filterpy.filterpy.stats as stats

import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt
import numpy.random as random
from numpy import dot
class KalmanFilter:
    def __init__(self, dim_x, dim_z, dim_u=0):
        """
        Create a Kalman filter. You are responsible for setting the
        various state variables to reasonable values; the defaults below will not give you a functional filter.
        Parameters
        ----------
        dim_x : int
        Number of state variables for the Kalman filter. For example, if
        you are tracking the position and velocity of an object in two
        dimensions, dim_x would be 4.
        This is used to set the default size of P, Q, and u
        dim_z : int
        Number of of measurement inputs. For example, if the sensor
        provides you with position in (x,y), dim_z would be 2.
        dim_u : int (optional)
        size of the control input, if it is being used.
        Default value of 0 indicates it is not used.
        """

        self.x = np.zeros((dim_x,1)) #state
        self.P = np.zeros(dim_x) # uncertainty covariance
        self.Q = np.zeros(dim_x) # process uncertainty
        self.u = np.zeros((dim_x,1)) # motion vector
        self.B = 0 #control transition matrix
        self.F = 0 #state transition function
        self.H = 0 # measurement function
        self.R = np.zeros(dim_x) # state uncertainty

        # identity matrix. Do not alter this.
        self._I = np.eye(dim_x)
        if use_short_form:
            self.update = self.update_short_form

    def update(self, Z, R=None):
        """
        Add a new measurement (Z) to the kalman filter. If Z is None, nothing
        is changed.
        Parameters
        ----------
        Z : np.array
        measurement for this update.
        R : np.array, scalar, or None
        Optionally provide R to override the measurement noise for this
        one call, otherwise self.R will be used.
        """
        if Z is None:
            return
        if R is None:
            R = self.R
        elif np.isscalar(R):
            R = np.eye(self.dim_z) * R

        # error (residual) between measurement and prediction
        y = Z - dot(H, x)
        # project system uncertainty into measurement space
        S = dot(H, P).dot(H.T) + R
        # map system uncertainty into kalman gain
        K = dot(P, H.T).dot(linalg.inv(S))
        # predict new x with residual scaled by the kalman gain
        self.x = self.x + dot(K, y)
        I_KH = self._I - dot(K, H)
        self.P = dot(I_KH).dot(P).dot(I_KH.T) + dot(K, R).dot(K.T)