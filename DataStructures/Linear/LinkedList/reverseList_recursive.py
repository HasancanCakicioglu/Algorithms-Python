from model.model_numbers   import *

def reverseListRecursive(head,prev=None):
    if(head == None):
        return prev
    next = head.next
    head.next = prev
    return reverseListRecursive(next,head)

print(reverseListRecursive(a).next.val)    