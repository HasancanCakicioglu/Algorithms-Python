
from Utility.shiftMethod import *
from model.model_1 import *

    



def breadthFirstValues(root):
    if root is None:
        return []
    values = []
    queue = [root]
    while(len(queue) > 0):
        current,queue = shiftList(queue)
        values.append(current.value)
        print(current.value)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)



br = breadthFirstValues(a)
print(br)       

