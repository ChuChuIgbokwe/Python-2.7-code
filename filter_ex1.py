#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 10, 2016 by 12:50 AM

values = [1, 2, 1, 3]
nums = set(values)

def checkit(num):
    if num in nums:
        return True
    else:
        return False

for i in  filter(checkit, values):
    print i



