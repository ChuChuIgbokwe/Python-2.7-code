#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 14, 2016 by 1:27 AM

qbfile = open("qbdata.txt", "r")

for aline in qbfile:
    values = aline.split()
    print'QB ', values[0], values[1], 'had a rating of ', values[10]

qbfile.close()




