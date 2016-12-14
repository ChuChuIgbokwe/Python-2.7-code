#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 26, 2016 by 3:58 PM

# explode('hello') = 'h e l l o'
def explode(word):
    if len(word) <= 1:
        # print word
        return word
    else:
        # print word
        return word[0] + ' ' + explode(word[1:])


print explode('hello')