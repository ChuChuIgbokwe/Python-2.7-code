#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 06, 2017 by 1:25 PM

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on January 05, 2017 by 1:10 PM

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

road_list = [('A', 2500, 4),
             ('B', 1000, 3),
             ('C', 1000, 4),
             ('D', 3500, 4),
             ('E', 4500, 3),
             ('F', 2255, 2),
             ('G', 1500, 1)]

intersection_list = [('A', 0,   'B', 180),
                     ('A', 0,   'D', 0),
                     ('A', 180, 'C', 0),
                     ('A', 255, 'F', 321),
                     ('B', 0,   'E', 0),
                     ('B', 180, 'A', 0),
                     ('B', 180, 'D', 0),
                     ('C', 0,   'A', 180),
                     ('C', 180, 'D', 180),
                     ('C', 180, 'E', 180),
                     ('C', 90,  'G', 50),
                     ('D', 0,   'A', 0),
                     ('D', 0,   'B', 180),
                     ('D', 180, 'C', 180),
                     ('D', 180, 'E', 180),
                     ('E', 0,   'B', 0),
                     ('E', 180, 'C', 180),
                     ('E', 180, 'D', 180),
                     ('E', 20,  'F', 214),
                     ('F', 214, 'E',20),
                     ('F', 321, 'A',255),
                     ('G', 50,  'C',90)]

initial_pose = [('F',355,'+')]
destination = [('G',230)]



#Helper Functions
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
    plt.show()
    check = nx.has_path(g,initial_pose[0][0],destination[0][0])
    if check == True:
        path = nx.shortest_path(g,initial_pose[0][0],destination[0][0])
    else:
        raise ValueError ("There is no path from {} to {}".format(initial_pose[0][0],destination[0][0]))

    j = 0
    path_tuples = []
    while j+1 < len(path):
        path_tuples.append((path[j],path[j+1]))
        j += 1
    path_length_tracker = len(path)

    road_dict = road_list_dict(road_list)
    commands_list,time_list = [],[]
    p = 0

    if path_length_tracker == 1:
        if initial_pose[0][2] == '+':  # clockwise
            angle_d = diff(initial_pose[0][1],destination[0][1])
        elif initial_pose[0][2] == '-':  # anti clockwise
            angle_d = diff(destination[0][0], initial_pose[0][1])
        else:
            raise ValueError('No drone orientation given')

        if angle_d < 0:
            commands_list.append('REVERSE')
        else:
            pass
        t = time_accelerating(road_dict[initial_pose[0][0]], abs(angle_d))
        commands_list.append('GO {}'.format(round(abs(t), 1)))
        time_list.append(round(abs(t), 1))
        time_list.append(0.1)

    else:

        while p < path_length_tracker:
            #initial traversal
            if p == 0:
                init_data = g.get_edge_data(path_tuples[p][0], path_tuples[p][1])['angles']
                if initial_pose[0][2]=='+': #clockwise
                    angle_d = diff(initial_pose[0][1], init_data[0])
                elif initial_pose[0][2]=='-': #anti clockwise
                    angle_d = diff(init_data[0],initial_pose[0][1])
                else:
                    raise ValueError('No drone orientation given')

                if angle_d < 0:
                    commands_list.append('REVERSE')
                else:
                    pass

                t = time_accelerating(road_dict[initial_pose[0][0]], abs(angle_d))
                commands_list.append('GO {}'.format(round(abs(t),1)))
                commands_list.append('TRANSFER {} {}'.format(path_tuples[p][1], 0.1))
                time_list.append(round(abs(t),1))
                time_list.append(0.1)
                p += 1

            #intermediary traversals
            elif p !=0 and p != path_length_tracker -1:
                starting_angle = init_data
                init_data = g.get_edge_data(path_tuples[p][0],path_tuples[p][1])['angles']
                angle_d = diff(starting_angle[1],init_data[0])

                if angle_d < 0:
                    commands_list.append('REVERSE')
                else:
                    pass

                t = time_accelerating(road_dict[path_tuples[p][0]], abs(angle_d))
                commands_list.append('GO {}'.format(round(abs(t),1)))
                commands_list.append('TRANSFER {} {}'.format(path_tuples[p][1], 0.1))
                time_list.append(round(abs(t),1))
                time_list.append(0.1)
                p += 1

            #final traversal
            elif p == path_length_tracker-1:
                starting_angle = init_data
                angle_d = diff(starting_angle[1],destination[0][1])
                if angle_d < 0:
                    commands_list.append('REVERSE')
                else:
                    pass

                t = time_accelerating(road_dict[destination[0][0]], abs(angle_d))
                commands_list.append('GO {}'.format(round(abs(t),1)))
                time_list.append(round(abs(t),1))
                time_list.append(0.1)
                p += 1

    print 'Start: ',initial_pose[0][0]
    print 'Destination: ',destination[0][0]
    print "Path Taken: ", path_tuples
    print "Total Time Takken: ",sum(time_list),'seconds\n'
    print "Drone Commands: \n"
    for i in commands_list:
        print i
        if i[0] == "T":
            print "Drone is now on {}\n".format(i[-5])
        if i == commands_list[-1]:
            print "Goal Reached!"
    return sum(time_list), commands_list

if __name__ == '__main__':
    drone_navigation()

