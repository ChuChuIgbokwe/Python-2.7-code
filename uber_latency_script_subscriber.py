#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 10, 2016 by 10:20 PM

import sys
import zmq
import time

# port = "5556"
# if len(sys.argv) > 1:
#     port =  sys.argv[1]
#     int(port)
#
# if len(sys.argv) > 2:
#     port1 =  sys.argv[2]
#     int(port1)

# Socket to talk to server
def subscriber():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    print 'connecting to publisher'
    socket.connect ("tcp://localhost:6464")

    # if len(sys.argv) > 2:
    #     socket.connect ("tcp://localhost:%s" % port1)
    topicfilter = "10001"
    socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

    total_value = 0
    while True:
        string = socket.recv()
        got_time = time.time()
        topic, msgdata = string.split()
        dur = got_time - float(msgdata)
        print 'it took %.5f from pub' % dur

if __name__=='__main__':
    subscriber()