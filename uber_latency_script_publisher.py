#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 10, 2016 by 10:15 PM

import zmq
import sys
import time

def publisher():
    # port = "5556"
    # if len(sys.argv) > 1:
    #     port =  sys.argv[1]
    #     int(port)

    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:6464" )

    topic = 10001
    while True:
        msgdata = time.time()
        socket.send("%d %.5f" % (topic, msgdata))
        print "topic:%d, msg:%.5f" % (topic, msgdata)
        time.sleep(1)



if __name__=='__main__':
    publisher()

