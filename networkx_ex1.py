#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 08, 2016 by 9:46 AM

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
# G.add_node('1')
# G.add_node('2')
# G.add_node('3')
# G.add_node('4')
# G.add_node('5')
# G.add_nodes_from(['1','2','3','4','5']) # You don't have to declare nodes
# G.add_edge('1','2')
# G.add_edge('2','3')
# G.add_edge('3','4')
# G.add_edge('4','1')
# G.add_edge('4','5')
#
# nx.draw_spectral(G)
# plt.show()

g = nx.DiGraph()
g.add_nodes_from(['1','2','3','4','5'])
g.add_edge('1','2')
g.add_edge('2','3')
g.add_edge('3','4')
g.add_edge('4','1')
g.add_edge('4','5')
nx.draw_spectral(g)
plt.show()