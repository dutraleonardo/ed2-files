#!/usr/bin/env python3
from binarytree import Node

class AvlTree:
    balanced_factor = 1

    def __init__(self, root=None, list_values=None):
        self.root = None if root is not None else root 
        if list_values is not None:
            self.bulk_insert(list_values)

    def bulk_insert(self, list_values):
        [self.insert(value) for value in list_values]

    def insert(self, value, node=None):
        self.root = Node(value) if (self.root == node == None) else self.root
        node = self.root if node is None else node
        bigger_than = value > node.value
        less_than = value < node.value

        if less_than and not (node.left is None):
            node = self.insert(value, node.left)
        elif less_than and node.left is None:
            node.left = Node(value)
            return
        if bigger_than and not (node.rig´´´ht is None):
            print(node.value, self.root.value)
            node = self.insert(value, node.right)
        elif bigger_than and node.right is None:
            node.right = Node(value)
            return
        else:
            self.balance(node)
    
    def balance(self, node):
        pass

    def display(self):
        print(self.root)
    
    def method(self):
        return self.insert.__name__