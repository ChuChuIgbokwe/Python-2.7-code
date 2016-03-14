#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 03, 2016 by 3:43 AM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys



img = cv2.cv.LoadImage("ronaldo.jpg")
dims = cv2.cv.GetSize(img)
roi = (0, 0, dims[0] / 2, dims[1] / 2 )
cv2.cv.SetImageROI(img, roi)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



