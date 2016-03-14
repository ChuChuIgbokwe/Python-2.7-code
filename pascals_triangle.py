#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 25, 2016 by 3:36 AM

# def pascal(n):
#     if n == 1:
#         return [1]
#     else:
#         p_line = pascal(n-1)
#         line = [ p_line[i]+p_line[i+1] for i in range(len(p_line)-1)]
#         line.insert(0,1)
#         line.append(1)
#     return line
#
# print(pascal(5))



def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

print(pascal(6))