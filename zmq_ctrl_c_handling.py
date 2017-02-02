#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 09, 2016 by 5:31 PM

#
#   Shows how to handle Ctrl-C
#
import signal
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5558")

# SIGINT will normally raise a KeyboardInterrupt, just like any other Python call
try:
    socket.recv()
except KeyboardInterrupt:
    print("W: interrupt received, stopping…")
finally:
    # clean up
    socket.close()
    context.term()