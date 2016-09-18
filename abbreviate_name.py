#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 15, 2016 by 6:48 PM

def abbreviate_name(name):
    name_split = name.split()
    name_length = len(name_split)
    abbreviation = ""
    surname = name_split[name_length-1]
    print surname
    for i in range(name_length-1):
        moniker = name_split[i]
        abbreviation += moniker[0]
        abbreviation += ". "

    print abbreviation + surname
    return abbreviation + surname



abbreviate_name("Bob Alan Faria Stewart")
abbreviate_name('John Smith')