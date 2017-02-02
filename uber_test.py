#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 10, 2016 by 6:29 PM


import zmq
import signal
import random
import names
import chicago
import threading
import multiprocessing
import time

def driver():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect("tcp://localhost:5570")
    # self.socket.setsockopt(zmq.IDENTITY, b"Driver")
    count = 0
    decision_options = ['accept'] * 9  + ['decline']
    ratings = [5.0] * 10 + [4.9] * 20 + [4.8] * 30 + [4.7] * 20 + [4.6] * 10 + [4.5] * 10
    chicago_neighbourhoods = [str(neighbourhood) for neighbourhood in chicago.NEIGHBORHOODS]

    while True:
        decision = random.choice(decision_options)
        driver_rating = str(random.choice(ratings))
        # fare = random.uniform(2.4,25.0)
        try:
            message = socket.recv_multipart()
            print("Received request: %s" % message)
            if float(message[2])> 4.5:
                socket.send(b"\nUber ETA: %s minutes\nDriver name %s\nDriver Rating: %s\n" % (
                random.randint(1, 10), names.get_first_name(), driver_rating))
                # self.count += 1
                # self.socket.send_multipart([str(self.count), str(fare)])
            else:
                socket.send(b"\n Your Driver Cancelled\n")
        except KeyboardInterrupt:
            socket.close()
            context.term()
            break

def passenger():
    #  Prepare our context and sockets
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5569")
# socket.setsockopt(zmq.IDENTITY, b"Passenger")
# socket.setsockopt(zmq.IDENTITY,passenger_name)
    chicago_neighbourhoods = [str(neighbourhood) for neighbourhood in chicago.NEIGHBORHOODS]
    ratings = [5.0] * 4 + [4.9] * 15 + [4.8] * 25 + [4.7] * 35 + [4.6] * 10 + [4.5] * 8 + [4.4] * 3
    #  Do 10 requests, waiting each time for a response
    for request in range(1,11):
        passenger_name = names.get_first_name()
        destination = random.choice(chicago_neighbourhoods)
        user_rating = str(random.choice(ratings))
        socket.send_multipart([str.encode(passenger_name),str.encode(destination),str.encode(user_rating)])
        message = socket.recv()
        # message_multi = socket.recv_multipart()
        print("Received reply %s [%s]" % (request, message))
        socket.close()
        context.term()

def UberApp():
    # Prepare our context and sockets
    context = zmq.Context()
    frontend = context.socket(zmq.ROUTER)
    frontend.setsockopt(zmq.IDENTITY, b"Uber App")
    backend = context.socket(zmq.DEALER)
    frontend.bind("tcp://*:5569")
    backend.bind("tcp://*:5570")

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

# def main():


passenger()
UberApp()
driver()

# main()

    # start = time.time()
    # while start > 10:
    #     d.callback()
    #     p.callback()
    #     u.callback()