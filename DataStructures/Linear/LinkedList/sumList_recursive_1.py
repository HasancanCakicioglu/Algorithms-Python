from model.model_numbers import *

def sumList(head):
    if(head == None):
        return 0
    return head.val + sumList(head.next)   

print(sumList(a))    