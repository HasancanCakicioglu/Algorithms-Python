class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

a = Node(val=1)
b = Node(val=2)
c = Node(val=3)
d = Node(val=4)

a.next = b
b.next = c
c.next = d