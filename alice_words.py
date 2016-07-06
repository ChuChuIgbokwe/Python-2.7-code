#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 15, 2016 by 3:11 AM


# with open('alice_in_wonderland.txt', 'r') as f:
#     data = [aline.split() for aline in f]



import string

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

def alice_words():
	'''
	Write a program called alice_words.py that creates a text file named
	alice_words.txt containing an alphabetical listing of all the words,
	and the number of times each occurs, in the text version of Alice’s
	Adventures in Wonderland.
	:return:
	'''

	with open("alice_in_wonderland.txt", "r") as f:
		aline = f.read()
	aline = aline.lower()
	aline_dict = dict()
	items = aline.split()

	for i in items:
		i = remove_punctuation(i)
		count = aline.count(i)
		aline_dict[i] = count

	# remove spaces
	aline_dict.pop('',None)
	#sort keys in alphabetical order
	keys = aline_dict.keys()
	keys.sort()
	out = open ("alice_word_count.txt","w")

	# for word in keys:
	# 	out.write(word + " " + str(aline_dict[word]))
	# 	out.write('\n')
	words = []
	for (k,v) in sorted(aline_dict.items()):
		# print  k, v
		words.append(v)

	# Get key by value in dictionary
	mode = aline_dict.keys()[aline_dict.values().index(max(words))]

	print "The word 'Alice' appears ",aline_dict['alice'], "times in this book"
	print "the longest word in Alice in Wonderland is",mode, "it has",max(words), "characters"

alice_words()