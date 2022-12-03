from model.model_numbers import *


def getNodeValues(head,index):
    current = head
    count = 0
    while current is not None:
        if(count == index): return current.val
        count += 1
        current = current.next
    return None

print(getNodeValues(a,1))        