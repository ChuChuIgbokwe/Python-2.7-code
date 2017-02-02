#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 10, 2016 by 6:02 PM

import zmq
import signal
import random
import names
import chicago
import threading
import multiprocessing
import time

# class Driver(object):
#     def __init__(self,id):
#         self.id = id
#         self.context = zmq.Context()
#         self.socket = self.context.socket(zmq.REP)
#         self.socket.connect("tcp://localhost:5560")
#         # self.socket.setsockopt(zmq.IDENTITY, b"Driver")
#         self.count = 0
#
#     def run(self):
#         identity = u'worker-%d' % self.id
#         self.socket.identity = identity.encode('ascii')



class Driver(object):
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.connect("tcp://localhost:5560")
        # self.socket.setsockopt(zmq.IDENTITY, b"Driver")
        self.count = 0


    def callback(self):
        decision_options = ['accept'] * 9  + ['decline']
        ratings = [5.0] * 10 + [4.9] * 20 + [4.8] * 30 + [4.7] * 20 + [4.6] * 10 + [4.5] * 10
        chicago_neighbourhoods = [str(neighbourhood) for neighbourhood in chicago.NEIGHBORHOODS]

        while True:
            decision = random.choice(decision_options)
            driver_rating = str(random.choice(ratings))
            # fare = random.uniform(2.4,25.0)
            try:
                message = self.socket.recv_multipart()
                print("Received request: %s" % message)
                if float(message[2])> 4.5:
                    self.socket.send(b"\nUber ETA: %s minutes\nDriver name %s\nDriver Rating: %s\n" % (
                    random.randint(1, 10), names.get_first_name(), driver_rating))
                    # self.count += 1
                    # self.socket.send_multipart([str(self.count), str(fare)])
                else:
                    self.socket.send(b"\n Your Driver Cancelled\n")
            except KeyboardInterrupt:
                self.socket.close()
                self.context.term()
                break

class Passenger(object):
    def __init__(self):
        #  Prepare our context and sockets
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:5559")
# socket.setsockopt(zmq.IDENTITY, b"Passenger")
# socket.setsockopt(zmq.IDENTITY,passenger_name)
    def callback(self):
        chicago_neighbourhoods = [str(neighbourhood) for neighbourhood in chicago.NEIGHBORHOODS]
        ratings = [5.0] * 4 + [4.9] * 15 + [4.8] * 25 + [4.7] * 35 + [4.6] * 10 + [4.5] * 8 + [4.4] * 3

        #  Do 10 requests, waiting each time for a response
        for request in range(1,11):
            passenger_name = names.get_first_name()
            destination = random.choice(chicago_neighbourhoods)
            user_rating = str(random.choice(ratings))
            self.socket.send_multipart([str.encode(passenger_name),str.encode(destination),str.encode(user_rating)])
            message = self.socket.recv()
            # message_multi = socket.recv_multipart()
            print("Received reply %s [%s]" % (request, message))

class UberApp(object):
    def __init__(self):
        # Prepare our context and sockets
        self.context = zmq.Context()
        self.frontend = self.context.socket(zmq.ROUTER)
        self.frontend.setsockopt(zmq.IDENTITY, b"Uber App")
        self.backend = self.context.socket(zmq.DEALER)
        self.frontend.bind("tcp://*:5559")
        self.backend.bind("tcp://*:5560")

        # Initialize poll set
        self.poller = zmq.Poller()
        self.poller.register(self.frontend, zmq.POLLIN)
        self.poller.register(self.backend, zmq.POLLIN)

    def callback(self):
        # Switch messages between sockets
        while True:
            try:
                socks = dict(self.poller.poll())
            except KeyboardInterrupt:
                break

            if socks.get(self.frontend) == zmq.POLLIN:
                message = self.frontend.recv_multipart()
                self.backend.send_multipart(message)

            if socks.get(self.backend) == zmq.POLLIN:
                message = self.backend.recv_multipart()
                self.frontend.send_multipart(message)

def main():
    d = Driver()
    p = Passenger
    u = UberApp
    start = time.time()
    while start > 10:
        d.callback()
        p.callback()
        u.callback()

