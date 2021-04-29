"""
In a doubly linked list, We define a linked list in which each node
keeps an explict reference to the node before it and a reference to the node after

These lists allow a greater variety of 0(1) - time update operation,
including insertions and deletions.

We continue to use the term "next" for the reference to the node that follows another

"""

class DoublyLinkListNode(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

a = DoublyLinkListNode(1)

b = DoublyLinkListNode(2)

c = DoublyLinkListNode(3)

a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b





