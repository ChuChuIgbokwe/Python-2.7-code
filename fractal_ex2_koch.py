#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 16, 2016 by 12:12 AM

import turtle

# def koch(t, order, size):
#     """
#        Make turtle t draw a Koch fractal of 'order' and 'size'.
#        Leave the turtle facing the same direction.
#     """
#
#     if order == 0:          # The base case is just a straight line
#         t.forward(size)
#     else:
#         koch(t, order-1, size/3)   # Go 1/3 of the way
#         t.left(60)
#         koch(t, order-1, size/3)
#         t.right(120)
#         koch(t, order-1, size/3)
#         t.left(60)
#         koch(t, order-1, size/3)

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)

def main():
	t = turtle.Turtle()
	myWin = turtle.Screen()
	koch(t,4,300)
	myWin.exitonclick()

main()



