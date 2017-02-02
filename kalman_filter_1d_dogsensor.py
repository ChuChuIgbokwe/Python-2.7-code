#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 29, 2017 by 1:22 AM

import numpy as np
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
        self.dt = 1

    def sense(self):
        self.x = self.x + self.velocity * self.dt #x0 = x + vt
        return self.x + np.random.randn() * self.noise

