#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 22, 2016 by 12:10 PM

def fib_to_sixty():    # write Fibonacci series up to n
        """Print a Fibonacci series up to n."""
        a, b = 0, 1
        fib_list = []
        while a < 2504730781961: #61st fibonacci number
            # print a,
            fib_list.append(a)
            a, b = b, a+b
	q = []
	how_many = int(raw_input('Enter how many numbers you want to search for:'))
	for i in range(how_many):
		num_elements = int(raw_input('Enter the numbers: '))
		q.append(num_elements)
	t = []
	for i in fib_list:
		for j in q:
			if j < i:
				# print i ,"\n"
				t.append(i)
				# for k in t:
				# 	if i > j:
				# 		t.remove(k)
	# t.sort()
	a = list(set(t))
	a.sort()
	for k in a:
		print k
fib_to_sixty()





