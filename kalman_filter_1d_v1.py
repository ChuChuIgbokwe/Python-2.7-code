#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 28, 2017 by 1:14 AM

from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt

# import numpy.random as random
import math
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

# dog = DogSensor(noise=0.0)
# xs = []
# for i in range(10):
#     x = dog.sense()
#     xs.append(x)
#     print ("%.4f" % x,end = ' ')
# plt.plot(xs, label='dog position')
# plt.legend(loc='best')
# plt.show()


def test_sensor(noise_scale):
    dog = DogSensor(noise=noise_scale)
    xs = []
    for i in range(100):
        x = dog.sense()
        xs.append(x)
    plt.plot(xs, label='sensor')
    plt.plot([0,99],[1,100], 'r--', label='actual')
    plt.xlabel('time')
    plt.ylabel('pos')
    plt.ylim([0,100])
    plt.title('noise = ' + str(noise_scale))
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

test_sensor(4.0)

dog = DogSensor(23, 0, 5)
xs = range(100)
ys = []
for i in xs:
    ys.append(dog.sense())
plt.plot(xs,ys, label='dog position')
plt.legend(loc='best')
plt.show()