from model.model_1 import *

def recursiveTreeIncludes(root,target):
    if root == None:
        return False
    if root.value == target:
        return True
    return recursiveTreeIncludes(root.left,target) or recursiveTreeIncludes(root.right,target)

print(recursiveTreeIncludes(a,"k"))    