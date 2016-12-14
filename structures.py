#!/usr/bin/env python
import numpy as np


class Data(object):
    '''class to store and pass data around my python code for HW0'''
    # x = []
    # y = []
    # theta = []

    def __init__(self):
        self.x = []
        self.y = []
        self.theta = []

    def append_data(self, x, y, theta):
        'function to append x, y, theta data point'
        self.x.append(x)
        self.y.append(y)
        self.theta.append(theta)
        # return self.x

        # pass





# def main():
#     # this does nothing, since we shouldn't be executing this file
#     nate = Data()
#     nate.append_data(2,3,4)
#     print nate.x
#     # pass
#
#
# main()
# if __name__ == '__main__':
#     try:
#         main()
#     except:
#         print "Something went wrong executing structures.py"
#     finally:
#         # put something here if you want it to run for ALL exceptions
#         pass
