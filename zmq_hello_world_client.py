#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 08, 2016 by 7:04 PM

'''
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
'''

import zmq
import time
context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
# for request in range(10):
#     print("Sending request %s …" % request)
#     socket.send_multipart(["Hello",'5'])
#
#     #  Get the reply.
#     message = socket.recv()
#     print("Received reply %s [ %s ]" % (request, message))

while True:
    first_time = socket.recv()
    got_time = time.time()
    socket.send_multipart([str(got_time)])
    # topic, msgdata = string.split()
    dur = got_time - float(first_time)
    print 'it took %.5f from pub' % dur