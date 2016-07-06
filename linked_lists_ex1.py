#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 14, 2016 by 7:06 PM

class Node(object):
    def __init__(self,init_data):
        self.data = init_data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,new_data):
        self.data = new_data

    def setNext(self,new_next):
        self.next = new_next



class UnorderedList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
		# if current is None:
		# 	raise ValueError("Data not in list")
		# return current
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        # if self.search(current) == False:
        #     raise ValueError("Data not in list")
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
		if current is None:
			raise ValueError("Data not in list")

		if previous == None:
			self.head = current.getNext()
			return current.getData()
		else:
			previous.setNext(current.getNext())
			return current.getData()

mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))

# mylist = UnorderedList()
# temp = Node(93)
# print temp.getData()
# temp.setData(77)
# print temp.getData()
# temp.setNext(33)
# print temp.getNext()
# print temp.getData()
#
# mylist.add(31)
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)
# # print mylist.search(33)
# print mylist.remove(54)

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
#
# node1.setNext(node2)
# node2.setNext(node3)
# print node2.getData()
#
# print node1.getNext()
# print node2.getNext()
#
#
# def printList(node):
#         while node:
#             print node,
#             node = node.getNext()
#         print
#
# printList(node1)