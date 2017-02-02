#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 09, 2016 by 5:32 PM

class Binarytree(object):
    '''
    A binary tree class where each node has a key/name and a left and right child
    '''
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = Binarytree(newNode)
        else:
            t = Binarytree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = Binarytree(newNode)
        else:
            t = Binarytree(newNode)
            t.rightChild = self.rightChild
            self.righttChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        return 'root = ' + str(self.key) +' ,left child = '+ str(self.leftChild)+ ' ,right child = ' + str(self.rightChild)

# r = Binarytree('a')
# print(r.getRootVal())
# # print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())

r = Binarytree('a')
print r.getRootVal()
print r
r.insertLeft('b')
r.insertRight('c')
print r
print r.getLeftChild().getRootVal()
r.getLeftChild().insertRight('d')
r.getRightChild().insertLeft('e')
r.getRightChild().insertRight('f')
print r
# print r.getRightChild().getRootVal()
# print r
# print r.getRootVal().insertRightChild('c')
# r.insertRight('c')
# r.setRootVal('b')
# r.insertRight('d')
# r.setRootVal('c')
# r.insertLeft('e')
# r.insertRight('f')
# print r.setRootVal('a')
# print r.getLeftChild()
# .getRootVal(),'d'
# r.insertRight(r.getRightChild(),'d')
# r.insertLeft(r.getLeftChild(),'e')
# r.insertRight(r.getRightChild(),'f')

# print r.getRightChild()


