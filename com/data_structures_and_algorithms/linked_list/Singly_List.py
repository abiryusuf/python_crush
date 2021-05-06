"""
A linked structure contains a collection of objects called nodes, each
of which contains data and at least one reference or link to another node. A linked
list is a linked structure in which the nodes are connected in sequence to form a linear
list
"""
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
# Three nodes
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = a


print(a.data)
print(a.next.data)
print(a.next.next.data)
print(a.next.next.next.data)


# Traversing the nodes
def traversal(head):
    curNode = head
    while curNode not in None:
        print(curNode.data)
        curNode = curNode.next


# Searching for a node
def unorderdSearch(head, target):
    curNode = head
    while curNode not in None and curNode.data != target:
        curNode = curNode.next
    return curNode is not None

