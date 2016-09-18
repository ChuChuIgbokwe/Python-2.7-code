#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on September 15, 2016 by 5:14 PM

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def is_valid_socket(address):
    checklist = []
    address_length = len(address)
    dot_index = list(find_all(address,'.'))
    colon_index = list(find_all(address,':'))
    start = 0
    number_check_dot = False
    number_check_colon = False
    another_checklist = []

    if len(dot_index) != 3 or len(colon_index) != 1:
        return False
    else:
        for i in range(3):
            check = address[start:dot_index[i]]
            checklist.append(check)
            start = dot_index[i]+1

        if int(address[colon_index[0] + 1:address_length]) >=1 and int(address[colon_index[0] + 1:address_length]) <= 65535:
            number_check_colon = True
        else:
            return False

        for i in checklist:
            if int(i) >= 0 and int(i) <= 255:
                another_checklist.append(int(i))
            else:
                return False

        if len(another_checklist) == 3:
            number_check_dot = True
        else:
            return  False

        if number_check_dot == number_check_colon:
            return True
        else:
            return False


print is_valid_socket('327.132.253.143:50')
print is_valid_socket('127.12.23.43:5000')
print is_valid_socket('127.A:-12')

