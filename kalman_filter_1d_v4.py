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
        self.dt = 1

    def sense(self):
        self.x = self.x + self.velocity * self.dt
        return self.x + np.random.randn() * self.noise

def multiply(mu1, var1, mu2, var2):
    mean = (var1*mu2 + var2*mu1) / (var1+var2)
    variance = 1 / (1/var1 + 1/var2)
    return (mean, variance)


def update(mean, variance, measurement, measurement_variance):
    return multiply(mean, variance, measurement, measurement_variance)

def predict(pos, variance, movement, movement_variance):
    return (pos + movement, variance + movement_variance)

# assume dog is always moving 1m to the right
movement = 0
movement_error = 2
sensor_error = 40
pos = (0, 100) # gaussian N(0,100)
dog = DogSensor(pos[0], velocity=movement, noise=sensor_error)
zs = []
ps = []
vs = []
for i in range(50):
    pos = predict(pos[0], pos[1], movement, movement_error)
    Z = dog.sense()
    zs.append(Z)
    vs.append(pos[1])
    pos = update(pos[0], pos[1], Z, sensor_error)
    ps.append(pos[0])

plt.figure(1)
plt.subplot(211)
plt.grid(True)
p1, = plt.plot(zs,c='r', linestyle='dashed')
p2, = plt.plot(ps,)
plt.legend([p1,p2], ['measurement', 'filter'], loc=2)
# plt.show()

plt.subplot(212)
plt.plot(vs)
plt.title('Variance')
plt.grid(True)
plt.show()
print ([float("%0.4f" % v) for v in vs])