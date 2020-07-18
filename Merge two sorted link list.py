#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    dummy = SinglyLinkedListNode(2)
    currD = dummy
    currA, currB = head1 , head2
    if currA == None:
        return(currB)
    elif currB == None :
        return(currA)
    while currA!=None and currB!=None:
        if currA.data < currB.data:
            temp = currA
            currA = currA.next
        elif currA.data > currB.data:
            temp = currB
            currB = currB.next
        else:
            temp = currA
            currA = currA.next
        currD.next = temp
        currD = currD.next
        
    currD.next = currA or currB
    return (dummy.next)
    
        
    


if __name__ == '__main__':