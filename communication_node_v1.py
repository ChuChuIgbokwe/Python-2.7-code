#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 08, 2016 by 10:53 AM


'''
Write a simple base "Communications Node" (CN) for a distributed communications system
running across multiple machines on a mixed (fast, slow, wired, WiFi, etc...) "local" network. In
its most basic form, each CN should have
    1. a unique ID and
    2. should come up and
    3. continuously enumerate all the other nodes it can see on its network:
    4. Update every 10-20 seconds
    5. List all other CNs on the reachable LAN (don’t worry about firewalls, NAT, etc...)
    6. Show round trip comms latency to every other node
    7. Show an estimate of "to" and "from" bandwidth with each other CN
    8. Implementation should allow an arbitrary number of CNs
    9. Implementation should allow multiple CNs to smoothly coexist on one machine

C or C++ with standard TCP and UDP socket calls is probably going to be the fastest route to
success on this task but we will accept alternative approaches.
    10. The best solution will not require manual setting of IP addresses, port numbers, or node IDs --
        these should be set automatically.

If time allows, implement some additional interesting features. For example:
    a.Provide statistics over time on performance, latencies, etc...
    b. Have nodes share connectivity information - find partially reachable nodes?
    c. Display a graphical map of node connectivity, link performance (ncurses?)
    d. Allow remote control, shutdown of nodes.
    e. Think of other fun/creative features!?
Test your code, run it on a variety of machines, and provide an example listing of the output.
'''
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import zmq
import time
import dispy
import random
import names

class CommunicationNode(object):
    def __init__(self,id):
        self.id = id

    def get_id(self):
        return self.id

node = CommunicationNode('A')
print node.get_id()

n = CommunicationNode('B')
print n.get_id()

G = nx.Graph()
G.add_edge(node.get_id(),n.get_id())
nx.draw_spectral(G)
plt.show()

import random
node_types = ['driver_node','passenger_node'] # driver- subscriber    passenger-publisher
#name broker uber_app
node_class = random.choice(node_types)
names.get_last_name()