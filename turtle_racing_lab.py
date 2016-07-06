#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 23, 2016 by 8:19 PM

import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-10,20)
lance.goto(-10,-20)

# your code goes here
for i in range(200):
	andy.forward(random.randrange(1,5))
	lance.forward(random.randrange(1,5))

wn.exitonclick()




