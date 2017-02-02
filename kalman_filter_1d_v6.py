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

sensor_error = 30
movement_error = 2
pos = (100,500)
zs = []
ps = []
for i in range(100):
    pos = predict(pos[0], pos[1], movement, movement_error)
    Z = math.sin(i/3.)*2 + np.random.randn()*1.2
    zs.append(Z)
    pos = update(pos[0], pos[1], Z, sensor_error)
    ps.append(pos[0])

p1, = plt.plot(zs,c='r', linestyle='dashed', label='measurement')
p2, = plt.plot(ps, c='#004080', label='filter')
plt.legend(loc='best')
plt.show()