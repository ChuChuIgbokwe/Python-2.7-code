#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 15, 2016 by 6:01 PM
import string

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

def palindrome(n):
	'''
	Write a function that takes a string as a parameter and returns True if the string is a palindrome,
	False otherwise. Remember that a string is a palindrome if it is spelled the same both forward and backward.
	for example: radar is a palindrome. for bonus points palindromes can also be phrases, but you need to remove
	the spaces and punctuation before checking. for example: madam i’m adam is a palindrome.
	:param n:
	:return:
	'''

	n = n.lower()
	n = remove_punctuation(n)
	n = n.replace(" ", "")  #remove spaces
	# print n

	if len(n)<= 1:
		return True
	elif n[0] == n[-1]:# compare first and last letters, if true remove them both and repeat
		return  palindrome(n[1:-1]) #n[1:-1] returns the middle letters or the word without the first and last letters
	else:
		return False

str = raw_input("Enter a string: ")
print palindrome(str)

'''
Other fun palindromes include:

kayak
aibohphobia
Live not on evil
Reviled did I live, said I, as evil I did deliver
Go hang a salami; I’m a lasagna hog.
Able was I ere I saw Elba
Kanakanak – a town in Alaska
Wassamassaw – a town in South Dakota
'''