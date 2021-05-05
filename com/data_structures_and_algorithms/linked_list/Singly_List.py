
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
# Three nodes
a = ListNode(12)
b = ListNode(53)
c = ListNode(43)
a.next = b
b.next = c


print(a.data)
print(a.next.data)
print(a.next.next.data)

