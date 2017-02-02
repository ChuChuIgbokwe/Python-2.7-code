#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 29, 2017 by 3:47 AM


from __future__ import division
import matplotlib.pyplot as plt
from filterpy.filterpy.kalman import KalmanFilter
import numpy as np


# Compare Multivariate Kalman Filter to Univariate Kalman Filter

# 1-D Kalman filter equations
def predict(pos, variance, movement, movement_variance):
    return (pos + movement, variance + movement_variance)

def update (mu1, var1, mu2, var2):
    mean = (var1*mu2 + var2*mu1) / (var1+var2)
    variance = 1 / (1/var1 + 1/var2)
    return (mean, variance)

def mkf_filter(R, Q):
    f = KalmanFilter(dim_x=1, dim_z=1, dim_u=1)
    f.P = 500.
    f.H = np.array([[1.]])
    f.F = np.array([[1.]])
    f.B = np.array([[1.]])
    f.Q = Q
    f.R = R
    return f

def plot_kf_compare(x0, p0, R, Q, move):
    # storage for filter output
    x1 = []
    x2 = []
    p1 = []
    p2 = []
    # initialize the filters
    f = mkf_filter(R, Q)
    f.x[0,0] = 0.
    f.P[0,0] = p0
    pos = (x0, p0)
    for i in range(50):
        z = i*move + np.random.randn()
        pos = update(pos[0], pos[1], z, R)
        f.update(z)
        x1.append(pos[0])
        x2.append(f.x[0,0])
        p1.append(pos[1])
        p2.append(f.P[0,0])
        u = move + np.random.randn()
        pos = predict(pos[0], pos[1], u, Q)
        f.predict(u=u)
    plt.scatter(range(len(x2)), x2, c='r')
    plt.title('State')
    plt.plot(x1)
    plt.figure()
    plt.plot(p1)
    plt.scatter(range(len(x2)), p2, c='r')
    plt.title('Variance')
    plt.show()


plot_kf_compare(x0=0., p0=500., R=5., Q=.2, move=1.)
# In this
# example velocity would the the unobserved variable. Write a Kalman filter that uses the
# state x = [x x]T  ̇ and compare it against the filter in the last exercise which used the state
# x = [x] .


def Q_DWPA(dim, dt=1., sigma=1.):
    """ Returns the Q matrix for the Discrete Wiener Process Acceleration Mode
    dim may be either 2 or 3, dt is the time step, and sigma is the variance i
    the noise"""
    assert dim == 2 or dim == 3
    if dim == 2:
        Q = np.array([[.25*dt**4,  .5*dt**3],
                      [ .5*dt**3,     dt**2]], dtype=float)
    else:
        Q = np.array([[.25*dt**4, .5*dt**3, .5*dt**2],
                      [ .5*dt**3,    dt**2,       dt],
                      [ .5*dt**2,     dt,          1]], dtype=float)
    return Q * sigma

def pos_vel_filter(R,Q):
    f = KalmanFilter(dim_x=2, dim_z=1)
    f.R = R
    f.Q = Q_DWPA(2, sigma=Q)
    f.F = np.array([[1,1],
    [0,1]])
    f.H = np.array([[1,0]])
    return f
# state transition matrix
# Measurement function

def plot_compare_pos_vel(x0, p0, R, Q, move):
    # storage for filter output
    x1 = []
    x2 = []
    # initialize the filters
    f1 = mkf_filter(R, Q)
    f1.x[0,0] = 0.
    f1.P[0,0] = p0
    f2 = pos_vel_filter(R, Q)
    f2.x[0,0] = 0.
    f2.x[1,0] = 1.
    f2.P *= p0
    for i in range(50):
        u = move + np.random.randn()
        f1.predict(u=u)
        f2.predict(u=u)
        z = i*move + np.random.randn()
        f1.update(z)
        f2.update(z)

        x1.append(f1.x[0, 0])
        x2.append(f2.x[0, 0])
    plt.plot(x1, label='1D Filter')
    plt.scatter(range(len(x2)), x2, c='r', label ='2D Filter')
    plt.title('State')
    plt.legend(loc=4)
    plt.show()

plot_compare_pos_vel(x0=0., p0=500., R=5., Q=.2, move=1.)