#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on February 25, 2016 by 3:39 AM
from math import sqrt
# def sieve(n):
'''
Implement a recursive function in Python for the sieve of Eratosthenes.
The sieve of Eratosthenes is a simple algorithm for finding all prime numbers up to a specified integer.
It was created by the ancient Greek mathematician Eratosthenes.
The algorithm to find all the prime numbers less than or equal to a given integer n:
	1.Create a list of integers from two to n: 2, 3, 4, ..., n
	2.Start with a counter i set to 2, i.e. the first prime number
	3.Starting from i+i, count up by i and remove those numbers from the list, i.e. 2*i, 3*i, 4*i, aso..
	4.Find the first number of the list following i. This is the next prime number.
	5.Set i to the number found in the previous step
	6.Repeat steps 3 and 4 until i is greater than n. (As an improvement: It's enough to go to the square root of n)
	7.All the numbers, which are still in the list, are prime numbers
You can easily see that we would be inefficient, if we strictly used this algorithm, e.g. we will try to remove the
multiples of 4, although they have been already removed by the multiples of 2. So it's enough to produce the
multiples of all the prime numbers up to the square root of n. We can recursively create these sets.
:param n:
:return:
'''

	# int_list = list(range(2,n+1))
	# i = 2
	# while i <= n:
	# for j in int_list:
	# 	if j*i in int_list == True:
	# 		int_list.remove(j)


def sieve(n):
	# returns all primes between 2 and n
	primes = list(range(2,n+1))
	max = sqrt(n)
	num = 2
	while num < max:
		i = num
		while i <= n:
			i += num #removes all num*i multiples
			if i in primes:
				primes.remove(i)
		for j in primes: #this allows you check succesvive elements in primes
			if j > num: #
				num = j #increase num
				break
	return primes

print(sieve(100))


def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

print primes_sieve2(100)