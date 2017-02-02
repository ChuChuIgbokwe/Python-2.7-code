#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 28, 2017 by 1:14 AM

# from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt

# import numpy.random as random
import math
import filterpy.filterpy.stats as stats
from kalman_filter_1d_equations import *
from  kalman_filter_1d_dogsensor import DogSensor

movement = 0
movement_error = 2
sensor_error = 3000 #low sensor accuracy
# movement_sensor = 30.0
pos = (1000,500) #bad initial position (0,500)
dog = DogSensor(0, velocity=movement, noise=sensor_error)
zs = []
ps = []
vs = []
for i in range(1000):
    # pos = update(pos[0], pos[1], movement, sensor_error)
    Z = dog.sense()
    zs.append(Z)
    pos = update(pos[0], pos[1], Z, sensor_error)
    ps.append(pos[0])
    vs.append(pos[1])
    pos = predict(pos[0], pos[1], movement+ np.random.randn(), movement_error)

plt.figure(1)
plt.subplot(211)
plt.plot(ps, label='filter')
plt.plot(zs, linestyle='dashed', c='r', label='measurement')
plt.legend()
# plt.show()
plt.subplot(212)
plt.plot(vs)
plt.title('Variance')
plt.show()