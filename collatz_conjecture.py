#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 12, 2016 by 12:09 PM


# def collatz_length(x):
#     # x = int(raw_input("Enter a number: "))
#     seq = [x]
#     if x<1:
#         return []
#     while x>1:
#         if x%2 == 0:
#             x = x / 2
#         else:
#             x = 3*x + 1
#         seq.append(x)
#     return len(seq)
#
# def collatz_check():
#     seq_length =[]
#     for i in range(1,1000001,1000):
#         print 'checking', i
#         seq_length.append(collatz_length(i))
#     max_no = max(seq_length)
#     max_index = seq_length.index(max_no) + 1
#     print max_no
#     print max_index
# collatz_check()

class collatz_conjecture(object):
    # def __init__(self):
    #     self.x = x

    def collatz_length(self,x):
        seq = [x]
        if x < 1:
            return []
        while x > 1:
            if x % 2 == 0:
                x = x / 2
            else:
                x = 3 * x + 1
            seq.append(x)
        return len(seq)

    def collatz_check(self):
        seq_length = []
        for i in range(1, 1000001, 1000):
            print 'checking', i
            seq_length.append(self.collatz_length(i))
        max_no = max(seq_length)
        max_index = seq_length.index(max_no) + 1
        print max_no
        print max_index

c = collatz_conjecture()
c.collatz_check()

