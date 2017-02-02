#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 07, 2016 by 5:25 PM

'''
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
'''
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv_multipart()
    print("Received request: %s" % message)


    #  Do some 'work'
    time.sleep(1)

    msgdata = time.time()
    # socket.send("%d %.5f" % (msgdata))
    # print "topic:%d, msg:%.5f" % (msgdata)
    time.sleep(1)

    #  Send reply back to client
    # encoded_message = str.encode(message[1])
    encoded_message = str.encode(msgdata)
    # socket.send(b"World")
    socket.send(encoded_message)