#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 16, 2016 by 2:06 AM

import turtle
def koch_0(t, size):
    t.forward(size)

def koch_1(t, size):
    for angle in [60, -120, 60, 0]:
       koch_0(t, size/3)
       t.left(angle)

def koch_2(t, size):
    for angle in [60, -120, 60, 0]:
       koch_1(t, size/3)
       t.left(angle)

def koch_3(t, size):
    for angle in [60, -120, 60, 0]:
       koch_2(t, size/3)
       t.left(angle)

def main():
	# turtle.setup(3200, 3200)
	t = turtle.Turtle()
	myWin = turtle.Screen()
	# koch_0(t,10)
	# koch_1(t,30)
	# koch_2(t,90)
	koch_3(t,270)

	myWin.exitonclick()

main()
