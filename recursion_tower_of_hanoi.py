#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 26, 2016 by 7:35 PM

# def moveTower(height,fromPole, toPole, withPole):
#     if height >= 1:
#         moveTower(height-1,fromPole,withPole,toPole)
#         moveDisk(fromPole,toPole)
#         moveTower(height-1,withPole,toPole,fromPole)
#
# def moveDisk(fp,tp):
#     print("moving disk from",fp,"to",tp)
#
# moveTower(3,"A","B","C")

# def moveTower(height, first_pole, middle_pole, end_pole):
#     if height >= 1:
#         moveTower(height - 1, first_pole, end_pole, middle_pole)
#         moveTower(1, first_pole,middle_pole, end_pole)
#         moveTower(height - 1, middle_pole,first_pole, end_pole)
#         moveDisk(first_pole, end_pole)
#
# def moveDisk(fp,tp):
#     print("moving disk from",fp,"to",tp)
#
# moveTower(3,"A","B","C")


def hanoi(n, first_pole, middle_pole, third_pole):
    '''
    Solve Tower of Hanoi
    :param n: int number of rings
    :param first_pole: string
    :param middle_pole: string
    :param third_pole: string
    :return:
    '''

    def print_move(fr, to):
        print "- Move top ring in '{}' tower to the '{}' tower".format(fr, to)

    if n == 1:
        print_move(first_pole, third_pole)

    else:
        hanoi(n - 1, first_pole, third_pole, middle_pole)
        hanoi(1, first_pole, middle_pole, third_pole)
        # hanoi(n - 1, C, B, A)
        hanoi(n - 1, middle_pole, first_pole, third_pole)

hanoi(4,'A','B','C')