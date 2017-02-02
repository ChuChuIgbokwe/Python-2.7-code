#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on March 10, 2016 by 9:40 PM

# def binarySearch(alist, item):
# 2	    first = 0
# 3	    last = len(alist)-1
# 4	    found = False
# 5
# 6	    while first<=last and not found:
# 7	        midpoint = (first + last)//2
# 8	        if alist[midpoint] == item:
# 9	            found = True
# 10	        else:
# 11	            if item < alist[midpoint]:
# 12	                last = midpoint-1
#             else:
#                 first = midpoint+1
#
# 	    return found
import bisect

def binarySearch(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist)//2
		if alist[midpoint]==item:
			return True,midpoint
		else:
			if item<alist[midpoint]:
				return binarySearch(alist[:midpoint],item)
			else:
				return binarySearch(alist[midpoint+1:],item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

print bisect.bisect_left(testlist,19)
