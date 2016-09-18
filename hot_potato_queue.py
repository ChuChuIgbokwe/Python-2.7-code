#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 14, 2016 by 10:47 AM

# from pythonds.basic.queue import Queue
# # import Queue
#
# def hotPotato(namelist, num):
#     simqueue = Queue()
#     for name in namelist:
#         simqueue.enqueue(name)
#
#     while simqueue.size() > 1:
#         for i in range(num):
#             simqueue.enqueue(simqueue.dequeue())
#
#         simqueue.dequeue()
#
#     return simqueue.dequeue()
#
# print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

import Queue

def hotPotato(namelist, num):
    simqueue = Queue.Queue()
    for name in namelist:
        simqueue.put(name)

    while simqueue.qsize() > 1:
        for i in range(num):
            simqueue.put(simqueue.get()) #remove first item on queue and put it at the back of the queue
        simqueue.get()

    return simqueue.get()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

