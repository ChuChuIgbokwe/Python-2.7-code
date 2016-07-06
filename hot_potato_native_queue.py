#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 14, 2016 by 12:12 PM

# from pythonds.basic.queue import Queue
import Queue

def hotPotato(namelist, num):
    simqueue = Queue.Queue()
    for name in namelist:
        simqueue.put(name)

    while simqueue.qsize() > 1:
        for i in range(num):
            simqueue.put(simqueue.get())

        simqueue.get()

    return simqueue.get()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))







