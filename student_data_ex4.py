#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 14, 2016 by 3:55 AM

import turtle
# import matplotlib.pyplot as plt


# def plotRegression():
# 	f = open("labdata.txt", "r")
# 	aline = f.readline()
# 	total_x = 0
# 	total_y = 0
# 	freq = 0
# 	summation_xy = 0
# 	sum_sqr_x = 0
# 	x_list = []
#
# 	for aline in f:
# 		items = aline.split()
# 		total_x += int(items[0])
# 		total_y += int(items[1])
# 		x_list.append(int(items[0]))
# 		freq += 1
# 		summation_xy += int(items[0])* int(items[1])
# 		sum_sqr_x += int(items[0])**2
#
# 	x_avg = float(total_x) / freq
# 	y_avg = float(total_y) / freq
#
# 	m = (summation_xy - freq * x_avg * y_avg) / (sum_sqr_x - freq * x_avg**2)
# 	# print x_avg, y_avg, freq,total_y,total_x , sum_sqr_x, summation_xy
# 	print m
#
#
# 	f.close()
#
# plotRegression()



def plotRegression(data):
	'''
	 """Interpret the data file labdata.txt such that each line contains an x,y
    coordinate pair. Write a function called plotRegression that reads the data
    from this file and uses a turtle to plot those points and a best fit line
    according to the following formulas:
    y=y¯+m(x−x¯)
    m=∑xiyi−nx¯y¯∑x2i−nx¯2
    where x¯ is the mean of the x-values, y¯ is the mean of the y- values and n
    is the number of points. If you are not familiar with the mathematical ∑ it
    is the sum operation. For example ∑xi means to add up all the x values.
    Your program should analyze the points and correctly scale the window using
    setworldcoordinates so that that each point can be plotted.
    Then you should draw the best fit line, in a different color, through the points."""
	:param data:
	:return:
	'''

	win = turtle.Screen()
	win.bgcolor('pink')

	t = turtle.Turtle()
	t.shape('circle')
	t.turtlesize(0.2)

	x_list, y_list = [i[0] for i in plot_data], [i[1] for i in plot_data]
	x_list, y_list = [float(i) for i in x_list], [float(i) for i in y_list]
	x_sum, y_sum = sum(x_list), sum(y_list)
	x_bar, y_bar = x_sum / len(x_list), y_sum / len(y_list)
	x_list_square = [i ** 2 for i in x_list]
	x_list_square_sum = sum(x_list_square)
	xy_list = [x_list[i] * y_list[i] for i in range(len(x_list))]
	xy_list_sum = sum(xy_list)

	m = (xy_list_sum - len(x_list) * x_bar * y_bar) / (x_list_square_sum - len(x_list) * x_bar ** 2)
	# print m
	# best y
	y_best = [ (y_bar + m * (x_list[i] - x_bar)) for i in range( len(x_list) ) ]

	# plot points

	max_x = max(x_list)
	max_y = max(y_list)
	win.setworldcoordinates(0, 0, max_x, max_y)
	for i in range(len(x_list)):
		t.penup()
		t.setposition(x_list[i], y_list[i])
		t.stamp()

	#plot best y
	t.penup()
	t.setposition(0,0)
	t.color('blue')
	for i in range(len(x_list)):
		t.setposition(x_list[i],y_best[i])
		t.pendown()

	win.exitonclick()

with open('labdata.txt', 'r') as f:
    plot_data = [aline.split() for aline in f]

plotRegression(plot_data)