#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 19, 2016 by 2:19 PM

def sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x >= arr[0]])


def quicksort(arr):
    """ Quicksort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if not arr:
        return []

    pivots = [x for x in arr if x == arr[0]]
    lesser = quicksort([x for x in arr if x < arr[0]])
    greater = quicksort([x for x in arr if x > arr[0]])

    return lesser + pivots + greater

def quicksort(arr):
    """ Quicksort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if not arr:
        return []

    return quicksort([x for x in arr if x < arr[0]]) \
        + [x for x in arr if x == arr[0]] \
        + quicksort([x for x in arr if x > arr[0]])


def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right