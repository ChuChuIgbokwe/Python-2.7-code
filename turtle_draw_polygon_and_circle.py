#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 23, 2016 by 9:43 PM

import turtle

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawCircle(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)


wn = turtle.Screen()
wheel = turtle.Turtle()

drawCircle(wheel, 20)

wn.exitonclick()




