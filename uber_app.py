#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 09, 2016 by 11:15 PM

# Simple request-reply broker
#
# Author: Lev Givon <lev(at)columbia(dot)edu>

import zmq


# Prepare our context and sockets
context = zmq.Context()
frontend = context.socket(zmq.ROUTER)
frontend.setsockopt(zmq.IDENTITY, b"Uber App")
backend = context.socket(zmq.DEALER)
frontend.bind("tcp://*:5559")
backend.bind("tcp://*:5560")

# Initialize poll set
poller = zmq.Poller()
poller.register(frontend, zmq.POLLIN)
poller.register(backend, zmq.POLLIN)

# Switch messages between sockets
while True:
    try:
        socks = dict(poller.poll())
    except KeyboardInterrupt:
        break

    if socks.get(frontend) == zmq.POLLIN:
        message = frontend.recv_multipart()
        backend.send_multipart(message)

    if socks.get(backend) == zmq.POLLIN:
        message = backend.recv_multipart()
        frontend.send_multipart(message)

    # zhelpers.dump(frontend)


