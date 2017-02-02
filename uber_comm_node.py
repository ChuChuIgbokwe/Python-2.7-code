#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Based on the load balancer of the zeromq guide by Brandon Carpenter
"""

import zmq
import random
import names
import chicago
import multiprocessing
import threading
import time
import networkx as nx
import matplotlib.pyplot as plt

PASSENGER_LIST = []
DRIVER_LIST = []

no_of_passengers = int(raw_input('How many passengers are there? '))
no_of_drivers = int(raw_input('How many drivers are there? '))

for i in range(no_of_passengers):
    PASSENGER_LIST.append(names.get_first_name())

for i in range(no_of_drivers):
    DRIVER_LIST.append(names.get_first_name())
timeout = 10.0

def passenger_request(ident):
    """Basic request-reply client using REQ socket."""
    socket = zmq.Context().socket(zmq.REQ)
    socket.identity = u"Passenger-{}".format(ident).encode("ascii")
    # print socket.identity
    socket.connect("ipc://frontend.ipc")

    chicago_neighbourhoods = [str(neighbourhood) for neighbourhood in chicago.NEIGHBORHOODS]
    ratings = [5.0] * 4 + [4.9] * 15 + [4.8] * 25 + [4.7] * 35 + [4.6] * 10 + [4.5] * 8 + [4.4] * 3
    destination = random.choice(chicago_neighbourhoods)
    user_rating = str(random.choice(ratings))
    # Send request, get reply
    tstart = time.time()
    socket.send(b"\nPassenger Name: %s \nPassenger Destination: %s \nPassenger Rating: %s\n" % (socket.identity,destination, user_rating))
    reply = socket.recv()
    tend = time.time()
    print ("----------------------------------------")
    print("Total elapsed time: %d msec" % ((tend - tstart) * 1000))
    print("{}: {}".format(socket.identity.decode("ascii"),
                          reply.decode("ascii")))

def driver_task(ident):
    """Worker task, using a REQ socket to do load-balancing."""
    socket = zmq.Context().socket(zmq.REQ)
    socket.identity = u"Driver-{}".format(ident).encode("ascii")
    socket.connect("ipc://backend.ipc")
    # socket.connect("tcp://localhost:6660")

    # Tell broker we're ready for work
    socket.send(b"READY")

    # decision_options = ['accept'] * 9 + ['decline']
    ratings = [5.0] * 10 + [4.9] * 20 + [4.8] * 30 + [4.7] * 20 + [4.6] * 10 + [4.5] * 10
    chicago_neighbourhoods = [str(neighbourhood) for neighbourhood in chicago.NEIGHBORHOODS]
    fare = str(round(random.uniform(2.4, 25.0),2))
    driver_rating = str(random.choice(ratings))

    while True:
        try:
            address, empty, request = socket.recv_multipart()
            print("{}: {}".format(socket.identity.decode("ascii"),
                                  request.decode("ascii")))

            # socket.send_multipart([address, b"", b"OKKK"])
            socket.send_multipart([address, driver_rating, fare])

        except KeyboardInterrupt:
            socket.close()
            zmq.Context().term()
            print "Interrupted"
            break
def UberApp():

    threading.Timer(10,UberApp).start() # update every 10 seconds
    """Load balancer main loop."""
    # Prepare context and sockets
    context = zmq.Context.instance()
    frontend = context.socket(zmq.ROUTER)
    frontend.bind("ipc://frontend.ipc")
    # frontend.bind("tcp://localhost:6659")
    backend = context.socket(zmq.ROUTER)
    backend.bind("ipc://backend.ipc")
    # backend.bind("tcp://localhost:6660")

    # Start background tasks
    def start(task, *args):
        process = multiprocessing.Process(target=task, args=args)
        process.daemon = True
        process.start()
    for i in PASSENGER_LIST:
        start(passenger_request, i)
    for i in DRIVER_LIST:
        start(driver_task, i)

    # Initialize main loop state
    count = len(PASSENGER_LIST)
    workers = []
    poller = zmq.Poller()
    # Only poll for requests from backend until workers are available
    poller.register(backend, zmq.POLLIN)

    while True:
        sockets = dict(poller.poll())

        if backend in sockets:
            # Handle worker activity on the backend

            request = backend.recv_multipart()

            worker, empty, client = request[:3]
            if not workers:
                # Poll for clients now that a worker is available
                poller.register(frontend, zmq.POLLIN)
            workers.append(worker)
            if client != b"READY" and len(request) > 3:
                # If client reply, send rest back to frontend
                empty, reply = request[3:]
                frontend.send_multipart([client, b"", reply])

                count -= 1
                if not count:
                    break

        if frontend in sockets:
            # Get next client request, route to last-used worker
            client, empty, request  = frontend.recv_multipart()
            worker = workers.pop(0)
            backend.send_multipart([worker, b"", client, b"", request])

            if not workers:
                # Don't poll clients if no workers are available
                poller.unregister(frontend)

    # Clean up
    backend.close()
    frontend.close()
    context.term()


def draw_graph():
    passenger_list = []
    driver_list =[]
    for i in PASSENGER_LIST:
        passenger_list.append(i + '-passenger')
    for i in DRIVER_LIST:
        driver_list.append(i +'-driver')
    values = passenger_list + driver_list
    star = nx.star_graph(len(values))
    values.insert(0, 'Uber App')
    keys = range(len(values))
    mapping = dict(zip(keys,values))
    star = nx.relabel_nodes(star, mapping)
    nx.draw(star, with_labels=True)
    plt.show()



if __name__ == "__main__":
    UberApp()
    # main()
    draw_graph()

