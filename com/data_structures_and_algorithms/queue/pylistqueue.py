"""

"""

class Queue:
    # create an empty queue
    def __init__(self):
        self.items = []

    # Returns True if the queue is empty
    def isEmpty(self):
        return self.items == []
    # Returns the number of items in the queue
    def __len__(self):
        return len(self.items)

    # Add the given items to the queue
    def enqueue(self, value):
        self.items.insert(0, value)

    # Removes the items from end of the list
    def dequeue(self):
        assert not self.isEmpty()
        return self.items.pop()
