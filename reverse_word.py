#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 15, 2016 by 8:19 PM

def reverseWord(word):
    reversed_word = []
    for i in word:
        reversed_word.insert(0,i)
    return ''.join(reversed_word[0:])

print reverseWord('qwe rty')

a = 'qwe rty'
print a[::-1]

def another_reverse(word):
    word_length = len(word) - 1
    reversed_word = ''
    while word_length >= 0:
        reversed_word += word[word_length]
        word_length -= 1
    return reversed_word

print another_reverse('qwe rty')
