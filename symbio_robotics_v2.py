#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 31, 2017 by 7:43 PM

# A spaceship has two seats and can hold up to 150 lbs.  Please write a function that takes as
# input a list of weights of a collection of robots and returns the minimum number of spaceships
# needed to transport ‘n’ robots in space.
# Now consider the list of weights to be integers, is there any change in the previous function to make it more efficient?


def minSpaceships(weight_list):
    modified_weight_list = [i for i in weight_list if i <= 150]
    modified_weight_list.sort()
    end = len(modified_weight_list)-1
    print modified_weight_list

    i = 0
    no_ships = 0
    start = 0

    if len(modified_weight_list) % 2 == 0:
        loops = len(modified_weight_list)/2+1
    else:
        loops = len(modified_weight_list)/2

    while i < loops : #iterate through half of the list
        current_weight = modified_weight_list[start] + modified_weight_list[end]
        if current_weight <= 150:
            no_ships += 1
            i += 1
            start += 1
            end -= 1
            if start == end: #handle middle elements in the list
                no_ships +=1
                break
            if start>end:
                break
        else:
            no_ships +=1 # this robot has to have one ship to itself as it's to heavy to share
            i += 1
            end -= 1 # compare the next biggest robot with your current robot

    return no_ships

print minSpaceships([325,23,45, 19.8,234,123,22,4.7,10.0,34,19,147])
print minSpaceships([200,99,23,45,75, 198,234,50,123,22,47,100,120,142,144])
print minSpaceships([22,23,43,44,50,75,99,100,120,123])
print minSpaceships([1,2,3,4,5])
print minSpaceships([120,121,122,123,30,31,29,32])


