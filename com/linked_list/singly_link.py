"""
A singly linked list, in its simplest form, is a collection of nodes that
collectively a liner sequence.

Each node stores a reference to an object that is an element
of the sequence, as well as a reference to the next node of the list
"""

class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None

a = Node(1)

b = Node(2)

c = Node(3)

a.nextnode = b

print(a.value)

print(a.nextnode.value)