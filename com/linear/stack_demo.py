"""
A linear is an ordered collection of items where the addition of new items
and the removal of existing items always takes place at the time same end
NOTE: last in - first out (LIFO)

A stack is a data structure that stores a liner collection of items with access
limited to a last-in first-out order

"""

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

# push(item) adds a new item to the top of the linear. it needs the item and return nothing

    def push(self, item):
        self.items.append(item)

# pop() removes the top item from the linear. It needs no parameters and return the nothing

    def pop(self):
        return self.items.pop()
# peek() return the top item from the linear but does not remove it. It needs no parameters.

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



s = Stack()


print(s.isEmpty())

print(s.push(1))

print(s.push("Two"))

print(s.peek())

print(s.push(True))

print(s.size())

print(s.isEmpty())

print(s.pop())
