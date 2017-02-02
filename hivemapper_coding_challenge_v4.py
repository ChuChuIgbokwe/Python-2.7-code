#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 09, 2017 by 9:34 PM


import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter

class DroneNavigation():
    def __init__(self,road_list,intersection_list, initial_pose,destination):
        self.road_list = road_list
        self.intersection_list = intersection_list
        self.initial_pose = initial_pose
        self.destination = destination

    def _road_list_dict(self,list_of_roads):
        '''
        Make a dictionary of road names and their corresponding radius
        :param list_of_roads:
        :return: dictionary containing road names as keys and their radius as values
        '''
        keys = [i[0] for i in list_of_roads]
        values = [i[1] for i in list_of_roads]
        d = dict(zip(keys, values))
        return d

    def _diff(self,angle1, angle2):
        '''
        return the difference between two angles on a circle
        :param angle1:
        :param angle2:
        :return:
        '''
        difference = angle2 - angle1
        if difference < -180:
            difference += 360
        if difference > 180:
            difference -= 360
        return difference

    def _time_accelerating(self,radius, angle):
        '''
        Calculate the arc length from subtended angle then  calculate the time taken to get to the next intersection
        while accelerating at 4m/s
        :param radius:
        :param angle:
        :return: time taken
        '''
        s = radius * ((angle * np.pi) / 180)
        t = ((s - 2) / 4.0) + 1
        return t

    def _input_check(self):
        '''
        Check you have the right number of intersections.
        :return: True or False
        '''
        intersection_count = 0
        True_Count = 0
        for i in range(len(road_list)):
            intersection_count += road_list[i][2]

        #check if each road has the right number of individual intersections
        if intersection_count == len(intersection_list):
            C = Counter(i[0] for i in intersection_list)
            for i in range(len(road_list)):
                if C[road_list[i][0]] == road_list[i][2]:
                    True_Count +=1
            if True_Count == len(road_list):
                return True
            else:
                return False
        else:
            return False


    def Navigate(self):
        g = nx.DiGraph()
        for i in range(len(self.intersection_list)):
            g.add_edge(self.intersection_list[i][0], self.intersection_list[i][2],
                       angles=[self.intersection_list[i][1], self.intersection_list[i][3]])
        nx.draw_circular(g, with_labels=True)
        plt.show()

        if self._input_check() == False:
            raise ValueError("You do not have the right number road of intersections")

        #Check if there's a path between initial position and goal
        path_check = nx.has_path(g, self.initial_pose[0][0], self.destination[0][0])
        if path_check == True:
            path = nx.shortest_path(g, self.initial_pose[0][0], self.destination[0][0])
        else:
            raise ValueError("There is no path from {} to {}".format(self.initial_pose[0][0], self.destination[0][0]))

        j = 0
        path_tuples = []
        while j + 1 < len(path):
            path_tuples.append((path[j], path[j + 1]))
            j += 1
        path_length_tracker = len(path)

        road_dict = self._road_list_dict(self.road_list)
        commands_list, time_list = [], [1] # 1 sec for stopping
        p = 0

        if path_length_tracker == 1:
            if self.initial_pose[0][2] == '+':  # clockwise
                angle_d = self._diff(self.initial_pose[0][1], self.destination[0][1])

            elif self.initial_pose[0][2] == '-':  # anti clockwise
                angle_d = self._diff(self.destination[0][1], self.initial_pose[0][1])
            else:
                raise ValueError('No drone orientation given')

            if angle_d < 0:
                commands_list.append('REVERSE {}'.format(0.3))
                time_list.append(0.3)
            else:
                pass
            t = self._time_accelerating(road_dict[self.initial_pose[0][0]], abs(angle_d))
            commands_list.append('GO {}'.format(round(abs(t), 1)))
            time_list.append(round(abs(t), 1))
            time_list.append(0.1)

        else:

            while p < path_length_tracker:
                # initial traversal
                if p == 0:
                    init_data = g.get_edge_data(path_tuples[p][0], path_tuples[p][1])['angles']
                    if self.initial_pose[0][2] == '+':  # clockwise
                        angle_d = self._diff(self.initial_pose[0][1], init_data[0])
                    elif self.initial_pose[0][2] == '-':  # anti clockwise
                        angle_d = self._diff(init_data[0], self.initial_pose[0][1])
                    else:
                        raise ValueError('No drone orientation given')

                    if angle_d < 0:
                        commands_list.append('REVERSE {}'.format(0.3))
                        time_list.append(0.3)
                    else:
                        pass

                    t = self._time_accelerating(road_dict[self.initial_pose[0][0]], abs(angle_d))
                    commands_list.append('GO {}'.format(round(abs(t), 1)))
                    commands_list.append('TRANSFER {} {}'.format(path_tuples[p][1], 0.1))
                    time_list.append(round(abs(t), 1))
                    time_list.append(0.1)
                    p += 1

                # intermediary traversals
                elif p != 0 and p != path_length_tracker - 1:
                    starting_angle = init_data
                    init_data = g.get_edge_data(path_tuples[p][0], path_tuples[p][1])['angles']
                    angle_d = self._diff(starting_angle[1], init_data[0])

                    if angle_d < 0:
                        commands_list.append('REVERSE {}'.format(0.3))
                        time_list.append(0.3)
                    else:
                        pass

                    t = self._time_accelerating(road_dict[path_tuples[p][0]], abs(angle_d))
                    commands_list.append('GO {}'.format(round(abs(t), 1)))
                    commands_list.append('TRANSFER {} {}'.format(path_tuples[p][1], 0.1))
                    time_list.append(round(abs(t), 1))
                    time_list.append(0.1)
                    p += 1

                # final traversal
                elif p == path_length_tracker - 1:
                    starting_angle = init_data
                    angle_d = self._diff(starting_angle[1], self.destination[0][1])
                    if angle_d < 0:
                        commands_list.append('REVERSE {}'.format(0.3))
                        time_list.append(0.3)
                    else:
                        pass

                    t = self._time_accelerating(road_dict[self.destination[0][0]], abs(angle_d))
                    commands_list.append('GO {}'.format(round(abs(t), 1)))
                    time_list.append(round(abs(t), 1))
                    time_list.append(0.1)
                    p += 1

        print 'Start: ', self.initial_pose[0][0]
        print 'Destination: ', self.destination[0][0]
        print "Path Taken: ", path_tuples
        print "Total Time Taken: ", sum(time_list), 'seconds\n'
        print "Drone Commands: \n"
        print "Drone is now on {}.".format(initial_pose[0][0])
        for i in commands_list:
            print i
            if i[0] == "T":
                print "\nDrone is now on {}".format(i[-5])
            if i == commands_list[-1]:
                print 'STOP'
                print "Goal Reached!"
        return sum(time_list), commands_list


road_list = [('A', 2500, 3),
             ('B', 1000, 3),
             ('C', 1000, 3),
             ('D', 3500, 4),
             ('E', 4500, 3)]

intersection_list = [('A', 0, 'B', 180),
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
                     ('E', 180, 'D', 180)]

initial_pose = [('E', 355, '+')]
destination = [('A', 0)]

D = DroneNavigation(road_list,intersection_list,initial_pose,destination)
D.Navigate()
