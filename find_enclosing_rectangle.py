#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 15, 2016 by 5:03 PM


def get_enclosing_rectangle(*args):
    x_list,y_list,w_list,h_list,numbers = ([] for i in range(5))
    #convert from tuple to string
    word = ''
    for i in args:
        word += i

    #remove letters
    extras = 'XYWH='
    for i in extras:
        word = word.replace(i,' ')
    word = word.split()
    #convert to integer
    numbers = [int(word[i]) for i in range(len(word))]
    #split into similar variables
    x_list = [numbers[i] for i in range(len(numbers)) if i % 4 == 0]
    y_list = [numbers[i] for i in range(len(numbers)) if i % 4 == 1]
    w_list = [numbers[i] for i in range(len(numbers)) if i % 4 == 2]
    h_list = [numbers[i] for i in range(len(numbers)) if i % 4 == 3]


    x_min, x_max = min(x_list), max(x_list)
    y_min, y_max = min(y_list), max(y_list)
    w_min, w_max = min(w_list), max(w_list)
    h_min, h_max = min(h_list), max(h_list)
    if x_min == 0:
        W = x_max + w_max
    else:
        W = x_max + w_max - x_min

    if y_min == 0:
        H = y_max + h_max
    else:
        H = y_max + h_max - y_min

    print"X=%d Y=%d W=%d H=%d"%(x_min,y_min,W,H)


get_enclosing_rectangle('X=5 Y=9 W=10 H=40', 'X=11 Y=79 W=10 H=40', 'X=12 Y=17 W=10 H=40', 'X=15 Y=9 W=10 H=40')
get_enclosing_rectangle('X=5 Y=9 W=10 H=40')
get_enclosing_rectangle('X=0 Y=0 W=1 H=5', 'X=0 Y=8 W=1 H=9')
