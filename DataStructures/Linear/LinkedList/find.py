from model.model_numbers import *

def linkedListFind(head,target):
    current = head
    while current is not None:
        if current.val == target:
            return True
        current = current.next
    return False

print(linkedListFind(a,32))            