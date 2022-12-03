from model.model_1 import *


def depthFirstValues(root):
    if root is None:
        return []
    
    leftValues = depthFirstValues(root.left)
    rightValues = depthFirstValues(root.right)
    return [ root.value, *leftValues, *rightValues ]


pr = depthFirstValues(a)
print(pr)