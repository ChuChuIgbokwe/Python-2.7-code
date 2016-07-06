#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on June 08, 2016 by 10:41 AM


towns = [{'name': 'Manchester', 'population': 58241}, {'name': 'Coventry', 'population': 12435}, {'name': 'South Windsor', 'population': 25709}]

'''
Create a new list of the town names using for loops... using list comprehensions... using the map() function.
'''
# For loops...
town_names = []
for town in towns:
    town_names.append(town.get('name'))
print town_names

# List comprehensions...
town_names = [town.get('name') for town in towns]
print town_names

# Map function...
town_names = map(lambda town: town.get('name'), towns)
print town_names

'''
Create two lists, one of the town names and one of the town populations using for loops...
using list comprehensions... using the zip() function.
'''
# For loops...
town_names = []
town_populations = []
for town in towns:
    town_names.append(town.get('name'))
    town_populations.append(town.get('population'))

# List comprehensions...
town_names = [town.get('name') for town in towns]
town_populations = [town.get('population') for town in towns]

# Zip function...
town_names, town_populations = zip(*[(town.get('name'), town.get('population')) for town in towns])
print town_names,town_populations

'''
Given the two lists (names and populations), combine them back into a list of dictionaries using for loops...
using list comprehensions.
'''

# For loops...
towns = []
for index, town_name in enumerate(town_names):
    town = {'name': town_name, 'population': town_populations[index]}
    towns.append(town)
# List comprehensions...
towns = [{
    'name': town_name,
    'population': town_populations[index]
} for index, town_name in enumerate(town_names)]

'''
Using the list of towns, find the total combined population using for loops...
using the sum() function... using the reduce() function.
'''

# For loops...
total_population = 0
for town in towns:
    total_population += town.get('population')
print total_population

# Sum function...
total_population = sum(town.get('population') for town in towns)
print total_population

# Reduce function...
total_population = reduce(lambda total, town: total + town.get('population'), towns, 0)
print total_population

# town_names = []
# town_populations = []
# for town in towns:
# 	town_names.append(town.get('name'))
# 	town_populations.append(town.get('population'))
#
# print town_names
# print town_populations
#
# # List comprehensions...
# town_names = [town.get('name') for town in towns]
# town_populations = [town.get('population') for town in towns]
#
# # Zip function...
# town_names, town_populations = zip(*[(town.get('name'), town.get('population')) for town in towns])
