"""
A queue is an ordered collection of items where the addition of new
items happens at one end
Note: first in  first out (FIFO), example: make a line in front of store
"""

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def