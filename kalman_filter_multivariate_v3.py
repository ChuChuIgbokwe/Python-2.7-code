#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 29, 2017 by 3:47 AM



import filterpy.filterpy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
from kalman_filter_1d_dogsensor import DogSensor
from filterpy.filterpy.kalman import KalmanFilter

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


def dog_tracking_filter(R,Q=0,cov=1.):
    dog_filter = KalmanFilter (dim_x=2, dim_z=1)
    dog_filter.x = np.array([[0],[0]])
    # initial state (location and velocity)
    dog_filter.F = np.array([[1,1],
                             [0,1]]) # state transition matrix
    dog_filter.H = np.array([[1,0]]) # Measurement function
    dog_filter.R *= R # measurement uncertainty
    dog_filter.P *= cov # covariance matrix

    if np.isscalar(Q):
        dog_filter.Q = Q_DWPA(2, sigma=Q)
    else:
        dog_filter.Q = Q
    return dog_filter


def filter_dog(noise=0, count=0, R=0, Q=0, P=500., data=None, initial_x=None):
    """ Kalman filter ’count’ readings from the DogSensor.
    ’noise’ is the noise scaling factor for the DogSensor.
    ’data’ provides the measurements. If set, noise will
    be ignored and data will not be generated for you.
    returns a tuple of (positions, measurements, covariance)
    """
    if data is None:
        dog = DogSensor(velocity=1, noise=noise)
        zs = [dog.sense() for t in range(count)]
    else:
        zs = data

    dog_filter = dog_tracking_filter(R=R, Q=Q, cov=P)
    if initial_x is not None:
        dog_filter.x = initial_x

    pos = [None] * count
    cov = [None] * count

    for t in range(count):
        z = zs[t]
        pos[t] = dog_filter.x[0,0]
        cov[t] = dog_filter.P

        # perform the kalman filter steps
        dog_filter.update (z)
        dog_filter.predict()

    return (pos, zs, cov)


def plot_track(noise=None, count=0, R=0, Q=0, P=500., initial_x=None, data=None, plot_P=True, title='Kalman Filter'):

    ps, zs, cov = filter_dog(noise=noise, data=data, count=count, R=R, Q=Q, P=P, initial_x=initial_x)

    p0, = plt.plot([0,count],[0,count])
    p1, = plt.plot(range(1,count+1),zs, linestyle='dashed')
    p2, = plt.plot(range(1,count+1),ps)
    plt.legend([p0,p1,p2], ['actual','measurement', 'filter'], loc=2)
    plt.ylim((0-10,count+10))
    plt.title(title)
    plt.show()

    if plot_P:
        plt.subplot(121)
        plot_covariance(cov, (0,0))
        plt.subplot(122)
        plot_covariance(cov, (1, 1))
        plt.show()

def plot_covariance(P, index=(0, 0)):
    ps = []

    for p in P:
        ps.append(p[index[0], index[1]])
    plt.plot(ps)

plot_track (noise=30, R=5, Q=0.01, count=100)

dog = DogSensor(velocity=1, noise=30)
zs = [dog.sense() for t in range(30)]
plot_track (data=zs, R=5, Q=10,count=30, plot_P=False, title='R = 5, Q = 10')
plot_track (data=zs, R=5, Q=.02,count=30, plot_P=False, title='R = 5, Q = 0.02')
plot_track (data=zs, R=1000, Q=0.1,count=30, plot_P=False, title='R = 1000, Q = 0.1')



def plot_track_ellipses(noise, count, R, Q=0, P=20., plot_P=True, title='Kalman'):
    dog = DogSensor(velocity=1, noise=noise)
    f = dog_tracking_filter(R=R, Q=Q, cov=P)
    ps = []
    zs = []
    cov = []
    for t in range (count):
        z = dog.sense()
        f.update (z)
        ps.append (f.x[0,0])
        cov.append(f.P)
        zs.append(z)
        f.predict()
    p0, = plt.plot([0,count],[0,count],'g', label='actual')
    p1, = plt.plot(range(1,count+1),zs,c='r', linestyle='dashed', label='measurement')
    p2, = plt.plot(range(1,count+1),ps, c='b', label='filter')
    plt.legend(loc='best')
    plt.title(title)

    for i,p in enumerate(cov):
        stats.plot_covariance_ellipse ((i+1, ps[i]), cov=p, axis_equal=False,facecolor='g', edgecolor=None, alpha=0.2)
        if i == len(cov)-1:
            s = ('$\sigma^2_{pos} = %.2f$' % p[0,0])
            plt.text (20,10,s,fontsize=18)
            s = ('$\sigma^2_{vel} = %.2f$' % p[1,1])
            plt.text (20,5,s,fontsize=18)
    #plt.xlim((-10,30))
    #plt.ylim((-10,40))
    plt.show()
plot_track_ellipses (noise=5, R=5, Q=.2, count=20, title='R = 5')
plot_track_ellipses (noise=5, R=.5, Q=.2, count=20, title='R = 0.5')
plot_track_ellipses (noise=0, R=500, Q=.2, count=7, title='R = 500')

x = np.array([325,23,45, 19.8,234,123,22,4.7,10.0,34,19,147],dtype=int)