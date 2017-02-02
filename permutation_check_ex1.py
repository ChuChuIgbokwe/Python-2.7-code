#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 27, 2016 by 3:31 PM

import collections

def same_permutation(a, b):
    d = collections.defaultdict(int)
    for x in a:
        d[x] += 1
    for x in b:
        d[x] -= 1
    return not any(d.itervalues())

## same_permutation([1,2,3],[2,3,1])
#. True

## same_permutation([1,2,3],[2,3,1,1])
#. False