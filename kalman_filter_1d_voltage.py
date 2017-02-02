#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 28, 2017 by 11:10 PM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys

from  kalman_filter_1d_class import KalmanFilter1D

'''
designing and implementing a Kalman filter for a thermometer. The
sensor for the thermometer outputs a voltage that corresponds to the temperature that is
being measured. We have read the manufacturer’s specifications for the sensor, and it tells
us that the sensor exhibits white noise with a standard deviation of 2.13.
'''
def volt(temp_variance):
    return np.random.randn()*temp_variance + 16.3

# def kf_volt():
temp_variance = 2.13**2
sensor_error = temp_variance
movement_error = .2
movement = 0
voltage = (25,1000) #who knows what the first value is?

N=50
zs = [volt(temp_variance) for i in range(N)]

ps = []
estimates = []


kf = KalmanFilter1D(x0=25, #initial state
                    P = 1000, # initial variance
                    R=temp_variance, #sensor noise
                    Q=movement_error) # movement noise



for i in range(N):
    kf.predict(movement)
    kf.update(zs[i])
    # save for latter plotting
    estimates.append(kf.x)
    ps.append(kf.P)

# plot the filter output and the variance
plt.figure(1)
plt.subplot(211)
plt.scatter(range(N), zs, marker='+', s=64, color='r', label='measurements')
p1, = plt.plot(estimates, label='filter')
plt.legend(loc='best')
plt.xlim((0,N));plt.ylim((0,30))
plt.grid(True)
# plt.show()

plt.subplot(212)
plt.plot(ps)
plt.title('Variance')
plt.grid(True)
plt.show()
print 'Variance converges to',ps[-1]
print 'Last voltage is', voltage[0]
# return estimates[-1]

# print  kf_volt()

# Write a function that runs the Kalman filter many times and
# record what value the voltage converges to each time. Plot this as a histogram. After 10,000
# runs do the results look normally distributed? Does this match your intuition of what should
# happen?
# vc =[]
# for i in range(10000):
#     a = kf_volt()
#     # print a
#     vc.append(a)
#
# print vc
# plt.hist(vc,bins=100)
# plt.show()


# def VKF():
#     voltage=(14,1000)
#     for i in range(N):
#         Z = volt(temp_variance)
#         voltage = update(voltage[0], voltage[1], Z, sensor_error)
#     return voltage[0]
# vs = []
# for i in range (10000):
#     vs.append (VKF())
# plt.hist(vs, bins=100, color='#e24a33')
# plt.show()