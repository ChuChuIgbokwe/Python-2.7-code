#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 27, 2016 by 2:24 PM

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        alist[fillslot],alist[positionOfMax] = alist[positionOfMax],alist[fillslot]
        # print alist
    return alist

print selectionSort([54,26,93,17,77,31,44,55,20])
