from model.model_2 import *


def recursiveTreeSum(root):
    if root is None:
        return 0
    else:
        return root.value + recursiveTreeSum(root.left) + recursiveTreeSum(root.right)

print(recursiveTreeSum(a))