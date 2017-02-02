#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on October 09, 2016 by 5:17 PM

from trees_binary_trees import *
def buildTree():
    t_root = BinaryTree('a')
    insertLeft(t_root,'b')
    insertRight(t_root,'c')
    insertRight(getLeftChild(t_root),'d')
    insertLeft(getRightChild(t_root),'e')
    insertRight(getRightChild(t_root),'f')
    return t_root

print buildTree()
