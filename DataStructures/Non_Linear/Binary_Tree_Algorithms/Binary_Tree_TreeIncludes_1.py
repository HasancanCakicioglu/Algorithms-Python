from Utility.shiftMethod import *
from model.model_1 import *

def treeIncludes(root,target):
    if root is None:
        return False
    
    queue = [root]
    
    while(len(queue) > 0):
        
        current,queue = shiftList(queue)

        if(current.value == target):
            return True


        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return False


print(treeIncludes(a, "c"))