#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 31, 2017 by 7:23 PM

# A spaceship has two seats and can hold up to 150 lbs.  Please write a function that takes as
# input a list of weights of a collection of robots and returns the minimum number of spaceships
# needed to transport ‘n’ robots in space.
# Now consider the list of weights to be integers, is there any change in the previous function to make it more efficient?


def minSpaceships(weight_list):
    weight_list.sort()
    i = 0
    no_ships = 0
    start = 0
    end = len(weight_list) - 1

    while i < len(weight_list) :
        current_weight = weight_list[start] + weight_list[end]
        if weight_list[end] > 150: #discard robots that weigh more than 150 lbs
            i += 1
            end -=1
        else:
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
print minSpaceships([150,149,1,4,5,6,6])
print minSpaceships([50,60,70,80])
print minSpaceships([50,60,70,110])
print minSpaceships([120,121,122,123,30,31,29,32])


#Using integers improves the performance by requiring less memory as they require only 8 bits of memory. There's no change
# i envisioned making to make the function more efficient