#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 31, 2017 by 8:39 PM

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib as mpl
import cv2, os, sys


# def minSpaceships(weight_list):
#     no_ships = 0
#     modified_weight_list = [i for i in weight_list if i <= 150]
#     # print modified_weight_list
#     modified_weight_list.sort()
#     start = 0
#     end = len(modified_weight_list)-1
#     print modified_weight_list
#     i = 0
#     second_set = []
#     while start<end:
#         if modified_weight_list[start] + modified_weight_list[end] <= 150:
#             no_ships +=1
#
#         else:
#             #move start
#
#
#     i = 0
#     j = len(m)
#     while i < j:
#         if a[i] + a[j] <= 150
#             ships += 1
#             a.remove(i)
#             a.remove(j)
#         elif a[i] + [j] < 150 and a[i] < len(a) / 2:
#             i += i
#
#         el

#
# def pairSum2(arr, k):
#     if len(arr)<2:
#         return
#     seen=set()
#     output=set()
#     for num in arr:
#         target=k-num
#         if target not in seen:
#             seen.add(num)
#         else:
#             output.add( (min(num, target), max(num, target)) )
#     print '\n'.join( map(str, list(output)) )
#
#
# pairSum2([200,99,23,45,75, 198,234,50,123,22,47,100,120,142,144],150)




#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 31, 2017 by 7:43 PM

# A spaceship has two seats and can hold up to 150 lbs.  Please write a function that takes as
# input a list of weights of a collection of robots and returns the minimum number of spaceships
# needed to transport ‘n’ robots in space.
# Now consider the list of weights to be integers, is there any change in the previous function to make it more efficient?


def minSpaceships(weight_list):
    no_ships = 0
    modified_weight_list = [i for i in weight_list if i <= 150]
    # print modified_weight_list
    modified_weight_list.sort()
    start = 0
    end = len(modified_weight_list)-1
    print modified_weight_list
    i = 0
    second_set = []

    while i < len(modified_weight_list)/2:
        # midpoint = len(modified_weight_list)/2
        # if midpoint - start == 1 and  end - midpoint == 1:
        #     no_ships+=1
        current_weight = modified_weight_list[start] + modified_weight_list[end]
        if current_weight <= 150:
            no_ships += 1
            i += 1
            start += 1
            end -= 1
        else:

            second_set.append(modified_weight_list[start])
            second_set.append(modified_weight_list[end])
            # no_ships += 2
            i += 1
            start += 1
            end -= 1
        # if len(modified_weight_list) % 2 == 1 and start +1  == len(modified_weight_list) / 2 -1:
        #     no_ships += 1
    second_set.sort()
    print second_set
    return no_ships

w_list = [200,23,45, 19.8,234,123,22,4.7,10.0,34,19,147]
# print minSpaceships(w_list)
print minSpaceships([200,99,23,45,75, 198,234,50,123,22,47,100,120,142,144])

i = 0
j = len(m)
while i<j:
    if a[i] + a[j] <= 150
        ships +=1
        a.remove(i)
        a.remove(j)
    elif a[i] + [j] < 150 and a[i] < len(a)/2:
        i +=i

    el
