#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 28, 2017 by 1:14 AM

from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt

# import numpy.random as random
import math
import filterpy.filterpy.stats as stats


class DogSensor(object):
    def __init__(self, x0=0, velocity=1, noise=0.0):
        """ x0 - initial position
        velocity - (+=right, -=left)
        noise - scaling factor for noise, 0== no noise
        """
        self.x = x0
        self.velocity = velocity
        self.noise = math.sqrt(noise)

    def sense(self):
        self.x = self.x + self.velocity
        return self.x + np.random.randn() * self.noise

def multiply(mu1, var1, mu2, var2):
    mean = (var1*mu2 + var2*mu1) / (var1+var2)
    variance = 1 / (1/var1 + 1/var2)
    return (mean, variance)

# xs = np.arange(16, 30, 0.1)
# m1,v1 = 23, 5
# m, v = multiply(m1,v1,m1,v1)

# ys = [stats.gaussian(x,m1,v1) for x in xs]
# plt.plot (xs, ys, label='original')
# ys = [stats.gaussian(x,m,v) for x in xs]
# plt.plot (xs, ys, label='multiply')
# plt.legend(loc='best')
# plt.show()

# m1, v1 = 23, 5
# m2, v2 = 25, 5
# m, s = multiply(m1,v1,m2,v2)
# ys = [stats.gaussian(x,m1,v1) for x in xs]
# plt.plot (xs, ys, label='measure 1')
# ys = [stats.gaussian(x,m2,v2) for x in xs]
# plt.plot (xs, ys, label='measure 2')
# ys = [stats.gaussian(x,m,v) for x in xs]
# plt.plot(xs, ys,label='multiply')
# plt.legend()
# plt.show()


xs = np.arange(0, 60, 0.1)
m1, v1 = 10, 5
m2, v2 = 50, 5
m, v = multiply(m1,v1,m2,v2)
ys = [stats.gaussian(x,m1,v1) for x in xs]
plt.plot (xs, ys, label='measure 1')
ys = [stats.gaussian(x,m2,v2) for x in xs]
plt.plot (xs, ys, label='measure 2')
ys = [stats.gaussian(x,m,v) for x in xs]
plt.plot(xs, ys, label='multiply')
plt.legend()
plt.show()

def update(mean, variance, measurement, measurement_variance):
    return multiply(mean, variance, measurement, measurement_variance)

def predict(pos, variance, movement, movement_variance):
    return (pos + movement, variance + movement_variance)

dog = DogSensor(velocity=0, noise=1)

pos,s = 2, 5
for i in range(20):
    pos,s = update(pos, s, dog.sense(), 5)
    print('time:', i, '\tposition =', "%.3f" % pos, '\tvariance =', "%.3f" % s)


# assume dog is always moving 1m to the right
movement = 1
movement_error = 2
sensor_error = 10
pos = (0, 500) # gaussian N(0,500)
dog = DogSensor(pos[0], velocity=movement, noise=sensor_error)
zs = []
ps = []
for i in range(10):
    pos = predict(pos[0], pos[1], movement, movement_error)
    print('PREDICT: {: 10.4f} {: 10.4f}'.format(pos[0], pos[1]),end='\t')
    Z = dog.sense()
    zs.append(Z)
    pos = update(pos[0], pos[1], Z, sensor_error)
    ps.append(pos[0])
    print('UPDATE: {: 10.4f} {: 10.4f}'.format(pos[0], pos[1]))
plt.plot(ps, label='filter')
plt.plot(zs, c='r', linestyle='dashed', label='measurement')
plt.legend(loc='best')
plt.grid(True)
plt.show()