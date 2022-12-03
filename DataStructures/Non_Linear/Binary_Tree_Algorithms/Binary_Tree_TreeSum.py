from model.model_2 import *
from Utility.shiftMethod import *

def treeSum(root):
    if root == None:
        return 0
    totalSum = 0
    queue = [root]

    while(len(queue)>0):
        current,queue = shiftList(queue)
        totalSum += current.value
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return totalSum


print(treeSum(a))