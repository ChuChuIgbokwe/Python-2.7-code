#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 08, 2016 by 10:27 AM

import networkx as nx
import matplotlib.pyplot as plt

# K_5 = nx.complete_graph(5)
# nx.draw(K_5)
# # plt.show()
#
# barbell = nx.barbell_graph(10,10)
# nx.draw(barbell)
# plt.show()

star = nx.star_graph(5)
mapping = {0:'oracle',1:'nightwing',2:'Alfred',3:'catwoman',4:'robin',5:'batman'}
star = nx.relabel_nodes(star,mapping)
nx.draw(star,with_labels=True)


plt.show()

# import threading
#
# def printit():
#   threading.Timer(5.0, printit).start()
#   print "Hello, World!"
#
# printit()