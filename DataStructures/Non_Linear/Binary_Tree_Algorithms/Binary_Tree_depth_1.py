
from model.model_1 import *

def depthFirstValues(root):
    if root is None:
        return []
        
    stack = [root]
    while(len(stack) > 0):
        current = stack.pop()
        print(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
            


depthFirstValues(a)