# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:55:42 2019

@author: sadash
"""

class Node:
    
    def __init__(self,pType,pos,color):
        self.prev = None
        self.next = None
        self.pType = pType
        self.pos = pos
        self.color = color
        
    @classmethod
    def getCopiedNode(cls,node):
        return cls(node.pType,node.pos,node.color)
    
    def __str__(self):
        return self.color+" "+self.pType+" "
    def __repr__(self):
        return str(self)
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insertNode(self,node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def deleteNode(self,node):
        if self.head == node:
            self.head = self.head.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            if node.next != None:
                node.next.prev = node.prev
                
    def __iter__(self):
        return ListIterator(self.head)
    
class ListIterator:
    
    def __init__(self,node):
        self.current = node
        
    def __next__(self):
        node = self.current
        if node == None:
            raise StopIteration
        else:
            self.current = node.next
            return node