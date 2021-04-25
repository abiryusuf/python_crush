"""
A stack is an ordered collection of items where the addition of new items
 and the removal of existing items always takes place at the time same end
NOTE: last in - first out (LIFO)
"""

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
# push(item) adds a new item to the top of the stack. it needs the item and return nothing

    def push(self, item):
        self.items.append(item)
# pop() removes the top item from the stack. It needs no parameters and return the nothing

    def pop(self):
        return self.items.pop()
# peek() return the top item from the stack but does not remove it. It needs no parameters.

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

s = Stack()


print(s.push(5))

print(s.isEmpty())

s.push("two")
s.push(3)

print(s.size())
