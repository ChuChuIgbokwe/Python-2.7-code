#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 06, 2017 by 1:10 PM

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


intersection_list = \
[('A', 0, 'B', 180),
 ('A', 0, 'D', 0),
 ('A', 180, 'C', 0),
 ('B', 0, 'E', 0),
 ('B', 180, 'A', 0),
 ('B', 180, 'D', 0),
 ('C', 0, 'A', 180),
 ('C', 180, 'D', 180),
 ('C', 180, 'E', 180),
 ('D', 0, 'A', 0),
 ('D', 0, 'B', 180),
 ('D', 180, 'C', 180),
 ('D', 180, 'E', 180),
 ('E', 0, 'B', 0),
 ('E', 180, 'C', 180),
 ('E', 180, 'D', 180),('F',214,'E',20),('F',322,'B',0)]

initial_pose = [('A',355,'+')]
destination = [('F',230)]
road_list =  [('A', 2500, 3), ('B', 1000, 3), ('C', 1000, 3), ('D', 3500, 4), ('E', 4500, 3),('F',2255,1)]

def road_list_dict(list_of_roads):
    keys = [i[0] for i in list_of_roads]
    values = [i[1] for i in list_of_roads]
    d = dict(zip(keys, values))
    return d



def diff(angle1,angle2):
    difference = angle2 - angle1
    if difference< -180:
        difference += 360
    if difference > 180:
        difference -= 360

    return difference

def time_accelerating(radius,angle):
    s = radius * ((angle * np.pi)/180)
    t = (s/4)-4
    return t

def drone_navigation():
    g = nx.DiGraph()
    for i in range(len(intersection_list)):
        g.add_edge(intersection_list[i][0],intersection_list[i][2],angles = [intersection_list[i][1],intersection_list[i][3]])
    nx.draw_circular(g,with_labels=True)
    # plt.show()

    # path = nx.shortest_path(g,initial_pose[0][0],destination[0][0])
    p = nx.shortest_path(g,'A','F')
    # p = nx.has_path(g,'A','F')
    pp = nx.all_pairs_shortest_path(g)
    print p

drone_navigation()