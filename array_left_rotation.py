#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 12, 2016 by 11:57 AM

# def array_left_rotation(a,n,k):
#     array = k
#     moves = 1
#     while moves <=n:
#         moving = k[0]
#         array.append(moving)
#         del k[0]
#         moves += 1
#     return array

# print array_left_rotation(20,10)

# def array_left_rotation(n,k):
#     array = [i for i in range(1, n + 1)]
#     moves = 1
#     while moves <=k:
#         moving = array[0]
#         array.append(moving)
#         del array[0]
#         moves += 1
#     return array
#
# print array_left_rotation(20,10)
# def array_left_rotation(a, n, k):
#     alist = list(a)
#     b = alist[k:]+alist[:k]
#     return b
#
def array_left_rotation(a,n,k):
  return a[k:]+a[:k]

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))

print array_left_rotation(5,4,[15,32,39,47,5])
# 20 10
# 41 73 89 7 10 1 59 58 84 77 77 97 58 1 86 58 26 10 86 51
