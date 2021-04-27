"""
A deque, also known as a double-ended queue, is an ordered collection
of items similar to the queue
It has to two ends, a front and a rear, and the items remain positioned in the collection
DIFFERENCE
What makes a deque different is the unrestricted nature of adding and removing items
New items can be added at either the front or the rear

It is important to note that even though the deque can assume many of the characteristics
of stacks and queues. it does not require the LIFO and FIFO ordering that are enforced by
those dara structures

it is up to make consistent use of the addition and removal operations
"""

class Deque(object):
    # Deque() creates a new deque that is empty. It needs no parameters and returns an empty
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

# addFront(item) add new item to the front deque. It needs the item and returns nothing

    def addFront(self, item):
        self.items.append(item)
# addRear(item) add new item to the rear of the deque. It needs the item and returns

    def addRear(self, item):
        self.items.insert(0, item)
# removeFront() removes the front item from the deque. It needs no parameters and return the item

    def removeFront(self):
        return self.items.pop()

# removeRear() removes the rear item from the deque
    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d = Deque()
d.addFront("hello")

d.addRear("World")

print(d.isEmpty())

print(d.size())

print(d.removeFront() + " " + d.removeRear())

