#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 14, 2016 by 10:50 PM

import turtle
'''
At the bottom of this page is a very long file called mystery.txt The lines of this file contain either the word UP or
DOWN or a pair of numbers. UP and DOWN are instructions for a turtle to lift up or put down its tail. The pairs of
numbers are some x,y coordinates. Write a program that reads the file mystery.txt and uses the turtle to draw the
picture described by the commands and the set of points.

'''
def mystery():
	'''
	 """At the end of this chapter is a very long file called mystery.txt The
    lines of this file contain either the word UP or DOWN or a pair of numbers.
    UP and DOWN are instructions for a turtle to lift up or put down its tail.
    The pair of numbers are some x,y coordinates. Write a program that reads the
    file mystery.txt and uses the turtle to draw the picture described by the
    commands and the set of points."""
	:return:
	'''

	wn = turtle.Screen()
	t = turtle.Turtle()
	t.speed(20)

	with open("mystery.txt", "r") as f:
		for line in f:
			line = line.strip()
			if line == "UP":
				t.up()
			elif line == "DOWN":
				t.down()
			else:
				x, y = map(int, line.split())
				t.setpos(x, y)

	wn.exitonclick()

# mystery()

def mys():
	t= turtle.Turtle()
	wn = turtle.Screen()
	wn.setworldcoordinates(-300,-300,300,300)

	with open("mystery.txt", "r") as f:
		for aline in f:
			items = aline.split()
			# i = aline.strip()
			# print type(i)
			if items[0] == "UP":
				t.penup()
			elif items[0]=="DOWN":
				t.pendown()
			else:
				t.goto(int(items[0]),int(items[1]))

	wn.exitonclick()

mys()