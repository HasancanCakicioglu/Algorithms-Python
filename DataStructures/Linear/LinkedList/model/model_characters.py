

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

# A -> B -> C -> D -> None