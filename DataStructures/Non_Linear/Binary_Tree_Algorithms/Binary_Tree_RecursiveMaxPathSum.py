import math
from model.model_2 import *


def maxPathSum(root):
    if root is None: return -math.inf
    if root.left is None and root.right is None: return root.value
    maxChildPathSum = max(maxPathSum(root.left), maxPathSum(root.right))
    return root.value + maxChildPathSum

print(maxPathSum(a))