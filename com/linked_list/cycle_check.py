"""
Given a singly linked list, write a function which takes in the first node
in a singly linked and return a boolean indicating if the linked list
contains a "cycle"

A cycle is when a node'S next point actually point back to previous node
in the list. Thin is also sometimes known as circularly linked list
"""

def cycle_check(node):

    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return True
    return False

print(cycle_check())
