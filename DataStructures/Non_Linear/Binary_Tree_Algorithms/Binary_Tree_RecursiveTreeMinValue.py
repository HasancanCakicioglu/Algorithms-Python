import math
from model.model_2 import *


def recursiveTreeMinValue(root):
    if(root == None): return math.inf

    leftMin = recursiveTreeMinValue(root.left)
    rightMin = recursiveTreeMinValue(root.right)
    return min(root.value, leftMin, rightMin)


print(recursiveTreeMinValue(a))