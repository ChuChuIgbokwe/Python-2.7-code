#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 12, 2016 by 5:38 PM

import random
'''
Create a list containing 100 random integers between 0 and 1000
(use iteration, append, and the random module). Write a function called average
that will take the list as a parameter and return the average.
'''
mylist = []
for i in range(100):
	mylist.append(random.randint(0, 1000))

def average(random_list):
	total_sum = 0
	for i in random_list:
		total_sum += i

	avg = total_sum/len(random_list)
	return avg

print average(mylist)




