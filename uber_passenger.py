#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 09, 2016 by 11:14 PM

#
#   Request-reply client in Python
#   Connects REQ socket to tcp://localhost:5559
#   Sends "Hello" to server, expects "World" back
#
import zmq
import chicago
import random
import names

#  Prepare our context and sockets
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5559")
# socket.setsockopt(zmq.IDENTITY, b"Passenger")
# socket.setsockopt(zmq.IDENTITY,passenger_name)
chicago_neighbourhoods = [str(neighbourhood) for neighbourhood in chicago.NEIGHBORHOODS]
ratings = [5.0] * 4 + [4.9] * 15 + [4.8] * 25 + [4.7] * 35 + [4.6] * 10 + [4.5] * 8 + [4.4] * 3

#  Do 10 requests, waiting each time for a response
for request in range(1,11):
    passenger_name = names.get_first_name()
    destination = random.choice(chicago_neighbourhoods)
    user_rating = str(random.choice(ratings))
    # data = [passenger_name,destination,user_rating]
    # socket.send(["%s %s"] % (str.encode(passenger_name),str.encode(destination)))
    # socket.send_multipart([b'black', b'yellow'])
    socket.send_multipart([str.encode(passenger_name),str.encode(destination),str.encode(user_rating)])
    message = socket.recv_multipart()
    # print message[0]
    # message_multi = socket.recv_multipart()
    print("Received reply %s [%s]" % (request, message))