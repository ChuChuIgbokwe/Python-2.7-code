#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 26, 2017 by 12:55 PM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
from math import *
from math import radians, cos, sin, asin, sqrt

class KalmanFilter:
    def __init__(self, A,H,x,P,Q,R):
        self.A = A
        self.H = H
        self.x = x
        self.P = P
        self.Q = Q
        self.R = R
        self.I = np.eye()
        self.gps_pos = np.loadtxt('nonexistent_gps_file.dat')
        self.latitude = self.gps_pos[0:,0]
        self.longitude = self.gps_pos[0:, 1]
        self.gps_velocity = self.gps_pos[0:, 2]



    def _update(self):
        pass

    def _predict(self):
        pass

    def _haversine(self):

        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians
        sz = len(self.longitude)
        distance_array = np.zeros(sz)
        bearing_array = np.zeros(sz)
        for i in range(len(self.longitude) - 1):
            self.longitude[i], self.latitude[i],self.longitude[i+1], self.latitude[i+1] = map(radians,[self.longitude[i], self.latitude[i],self.longitude[i+1]])
            # haversine formula
            dlon = self.longitude[i+1] - self.longitude[i]
            dlat = self.latitude[i+1] - self.latitude[i]
            a = sin(dlat / 2) ** 2 + cos(self.latitude[i]) * cos(self.latitude[i+1]) * sin(dlon / 2) ** 2
            c = 2 * asin(sqrt(a))
            r = 6371  # Radius of earth in kilometers.
            distance_array[i+1] = (c * r)/100.0 #initial distance will be zero

            bearing = atan2(sin(self.longitude[i+1] - self.longitude[i]) * cos(self.latitude[i+1]),
                        cos(self.latitude[i]) * sin(self.latitude[i+1]) - sin(self.latitude[i]) * cos(self.latitude[i+1]) * cos(self.longitude[i+1] - self.longitude[i]))
            bearing = degrees(bearing)
            bearing = (bearing + 360) % 360
            bearing_array[i+1] = bearing #initial heading will be zero

        return np.vstack((distance_array,bearing_array)).T
