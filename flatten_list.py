#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 27, 2016 by 12:08 PM

import itertools

def flatten(l):
    return [item for sublist in l for item in sublist]

def flatten_1(l):
    return list(itertools.chain.from_iterable(l))

def flatten_2(data):
    """Recursive way to flatten a list."""
    if data is None or len(data) == 0:
      return data
    else:
      result = []
      for item in data:
        if isinstance(item, list):
          result.extend(flatten_2(item))
        elif item != '':
          result.append(item)
      return result

def flatten_3(l):
    return sum(l,[])


def f(l):
    x = []
    for sublist in l:
        for item in sublist:
            x.append(item)

    return x


list2d = [[1,2,3],[4,5,6], [7], [8,9]]
print flatten(list2d)
print flatten_1(list2d)
print flatten_2(list2d)
print flatten_3(list2d)
print f(list2d)


