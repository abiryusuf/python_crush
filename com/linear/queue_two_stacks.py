"""
Given the stack class below, implement a queue class using two stacks.

The key insight is that a stack reverses order (while a queue doesn't).
A sequence of elements pushed on a stack comes back in reversed order when popped.
Consequently, two stacks chained together will return elements in the same order,
since reversed order reversed again is original order.
We use an in-stack that we fill when an element is enqueued and the dequeue operation
takes elements from an out-stack. If the out-stack is empty we pop all elements from the
in-stack and push them onto the out-stack.
"""

class Queue2Stacks(object):

    def __init__(self):
        # Two stacks
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        # Add an enqueue with the "IN" stack
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                # Add the elements to the outstack to reverse the order when called
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

q = Queue2Stacks()

for i in range(5):
    print(q.enqueue(i))



