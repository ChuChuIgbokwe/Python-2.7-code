#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 09, 2016 by 11:15 PM

#
#   Request-reply service in Python
#   Connects REP socket to tcp://localhost:5560
#   Expects "Hello" from client, replies with "World"
#
import zmq
import signal
import random
import names
import chicago

# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.connect("tcp://localhost:5560")
#
# while True:
#     message = socket.recv()
#     print("Received request: %s" % message)
#     socket.send(b"World")


class driver(object):
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
                # if
                print("Received request: %s" % message)
                # if decision == 'accept':
                if float(message[2])> 4.5:
                # self.socket.send(b"World")
                # self.socket.send(str.encode(message[0]))
                #     self.socket.send(b"\nUber ETA: %s minutes\nDriver name %s\nDriver Rating: %s\n" % (
                #     random.randint(1, 10), names.get_first_name(), driver_rating))
                    self.socket.send_multipart([names.get_first_name(),driver_rating])
                    # self.count += 1
                    # self.socket.send_multipart([str(self.count), str(fare)])
                else:
                    self.socket.send(b"\n Your Driver Cancelled\n")
            except KeyboardInterrupt:
                self.socket.close()
                self.context.term()
                break
            # finally:
            #     # clean up
            #     self.socket.close()
            #     self.context.term()


d = driver()
# while True:
d.callback()
