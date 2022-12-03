from model.model_numbers import *


def getNodeValuesRecursive(head,index):
    if(head == None):
        return None
    if(index == 0):
        return head.val
    return getNodeValuesRecursive(head.next,index-1)

print(getNodeValuesRecursive(a,3))        