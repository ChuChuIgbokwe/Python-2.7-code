#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 11, 2016 by 10:18 AM

class Tree(object):
    def __init__(self,parent, leftChild=None, rightChild=None):
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild

    def __str__(self):
        return 'parent = ' + str(self.parent) + ' ,left child of ' + str(self.parent) + ' = ' + str(self.leftChild) + ' ,right child of ' + str(self.parent) +' = ' + str(
            self.rightChild)

#Building trees from the bottom up
# left = Tree(2)
# right = Tree(3)
# tree = Tree(1,left,right)
# print tree
# tree = Tree(1,Tree(2),Tree(3))
# print tree

R = Tree('c','e','f')
L = Tree('b',rightChild='d')
root = Tree('a',L,R)
print root

def total(tree):
    if tree == None:
        return 0
    return total(tree.leftChild) + total(tree.rightChild) + tree.parent

def print_tree(tree):
    if tree == None: return
    print tree.parent
    print_tree(tree.leftChild)
    print_tree(tree.rightChild)

tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
print_tree(tree)
print tree