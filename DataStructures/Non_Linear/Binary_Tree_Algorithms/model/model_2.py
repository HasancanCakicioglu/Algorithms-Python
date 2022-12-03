class NodeInt:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = NodeInt(10)
b = NodeInt(3)
c = NodeInt(9)
d = NodeInt(24)
e = NodeInt(1)
f = NodeInt(8)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f



            #         a
            #       /   \
            #      b     c
            #     / \     \
            #    d   e     f 