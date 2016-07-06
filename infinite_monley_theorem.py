#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 24, 2016 by 2:01 AM

'''
How long do you think it would take for a Python function to generate just one sentence of Shakespeare?
The sentence we’ll shoot for is: “methinks it is like a weasel”
The way we’ll simulate this is to write a function that generates a string that is 27 characters long by choosing
random letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each
generated string by comparing the randomly generated string to the goal.

A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.
If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s
progress this third function should print out the best string generated so far and its score every 1000 tries.
'''
import random
sentence = "methinks it is like a weasel"
sentence_list = [ch for ch in sentence]
# print len(sentence_list)

def theorem():
	alphabet = 'abcdefghijklmnopqrstuvwxyz '
	alphabet_list  = [ch for ch in alphabet]
	# print alphabet_list
	random_list = [random.choice(alphabet_list) for i in range(28)]
	# print len(random_list)
	return random_list
# theorem()
# theorem()
def accuracy():
	count = 0
	new_string = theorem()
	# print new_string
	# print sentence_list
	for i in range(28):
		if sentence_list[i] == new_string[i]:
			count +=1
	percentage = (count/28.0) * 100
	# print percentage,"%"
	return percentage,new_string
# accuracy()
def to_infinity():
	score = accuracy()
	# print score[0]
	# print score
	temp_score=[]
	tries = 0
	while score[0] != 100:
		accuracy()
		tries +=1
		temp_score.append(score)
		if tries % 1000 == 0:
		# 	tries = 0

			temp_score = [max(temp_score)]

			print temp_score
			break

to_infinity()

