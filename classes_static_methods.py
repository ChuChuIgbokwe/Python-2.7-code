#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 14, 2016 by 2:24 AM

class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

	@staticmethod
	def make_car_sound():
		print 'VRooooommmm!'



mustang = Car('Ford', 'Mustang')
mustang.make_car_sound
