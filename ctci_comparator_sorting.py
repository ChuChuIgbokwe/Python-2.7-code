#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 18, 2016 by 8:15 PM

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return '%s %d'%(self.name,self,score)

    def comparator(a, b):
        # if a.score < b.score:
        #     a,b = b,a
        # if a.score > b.score:
        #     pass
        if a.score == b.score and a.name != b.name:
            return a.score > b.score
        else:
            return a.name<b.name


n = int(raw_input())
data = []
for i in range(n):
    name, score = raw_input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, cmp=Player.comparator)
for i in data:
    print i.name, i.score