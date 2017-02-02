#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 15, 2016 by 11:19 PM

def rotate(Matrix):
    return zip(*Matrix[::-1])

print rotate([[1,2,3],[4,5,6],[7,8,9]])

def zip(seq1, seq2):
    out = []
    for i in range(len(seq1)):
        out.append((seq1[i], seq2[i]))

    return out



def reverse_list_of_lists(list_of_lists):
    new_list= []
    for i in list_of_lists:
        new_list.insert(0,i)

    return new_list

# print reverse_list_of_lists([[1,2,3],[4,5,6],[7,8,9]])

# def another_rotate(Matrix):
#     reversed_Matrix = reverse_list_of_lists(Matrix)
#     for