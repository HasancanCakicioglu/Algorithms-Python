from model.model_numbers import *
 

def sumList(head : Node)->Node:
    
    sum = 0
    current : Node = head
    while(current != None):
        sum += current.val
        current = current.next
    return sum;    

print(sumList(a))