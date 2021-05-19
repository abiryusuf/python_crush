"""
A queue is an ordered collection of items where the addition of new
items happens at one end
Note: first in  first out (FIFO), example: make a line in front of store
"""

class Queue(object):
    # Queue() create a new queue that is empty. It needs no parameters and return an empty queue

    def __init__(self):
        self.items = []
# isEmpty() tests to see whether the queue is empty. It needs no parameters and returns the item

    def isEmpty(self):
        return self.items == []

# enqueue(items) adds a new item to the rear of the queue. It needs the item and returns nothing

    def enqueue(self, item):
        self.items.insert(0, item)
# dequeue() removes the front item from the queue. it needs no parameters and returns the items

    def dequeue(self):
        return self.items.pop()
# size() return the number of items in the queue. it needs no parameters and returns an integer

    def size(self):
        return len(self.items)

q = Queue()

r = q.size()
print(r)

q.enqueue(3)


q.enqueue(3, "red")



