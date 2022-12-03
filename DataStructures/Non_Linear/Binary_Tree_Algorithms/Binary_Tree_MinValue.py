import math
from model.model_2 import *


def treeMinValue(root):
    smallest = math.inf
    stack = [root]
    while(len(stack) > 0):
        current = stack.pop()
        if current.value < smallest:
            smallest = current.value

        if current.left is not None:
            stack.append(current.left)    
        if current.right is not None:
            stack.append(current.right)
    return smallest        
        

print(treeMinValue(a))