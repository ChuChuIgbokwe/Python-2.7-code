#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 19, 2016 by 2:36 PM

nums = [1,2,3,4,5,6,7,8,9,10]
my_list = []
for n in nums:
	my_list.append(n)
print 'for loop and append', my_list

# list comprehension
my_list = [n for n in nums]
print my_list

#I want 'n*n' for each 'n' in nums
# list squared via list comprehension
my_list = [n*n for n in nums]
print my_list

def sqr_num(nums):
	return nums**2

# function and map
my_list = map(sqr_num,nums)
print  my_list

# map & lambda
my_list = map(lambda n: n*n, nums)
print  my_list

# even numbers
my_list = []
for n in nums:
	if n%2 == 0:
		my_list.append(n)
print  my_list

my_list = [n for n in nums if n%2 == 0]
print my_list

# filter and lambda
my_list = filter(lambda n: n%2 == 0, nums)
print my_list

#I want a (letter,num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
	for num in range(4):
		my_list.append((letter,num))
print my_list

my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print my_list

#Dictionary Comprehensions
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]
# print zip(names,heros)
#  I want a dict{"name": "hero"} for each name,hero in zip(name, heros)
my_dict = {}
for name, hero in zip(names, heros):
	my_dict[name] = hero
print my_dict

#Dictionary Comprehension
my_dict = {name:hero for name, hero in zip(names,heros) if name != 'Peter'}
print my_dict

nums = [1,1,2,1,3,4,3,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
	my_set.add(n)
# my_set = set(nums)
print my_set

my_set = {n for n in nums}
print my_set