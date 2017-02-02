#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 07, 2016 by 10:12 PM

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch, [], []])

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

# r = BinaryTree(3)
# print r
# print ''
# insertLeft(r,4)
# print r
# print ''
# insertLeft(r,5)
# print r
# print ''
# insertRight(r,6)
# insertRight(r,7)
# print r
# print ''
# l = getLeftChild(r)
# print l
# print ''
#
# setRootVal(l,9)
# print r
# print ''
# insertLeft(l,11)
# print r
# print ''
# print getRightChild(getRightChild(r))
#
x = BinaryTree('a')
insertLeft(x,'b')
insertRight(x,'c')
insertRight(getRightChild(x),'d')
insertLeft(getRightChild(getRightChild(x)),'e')
print x