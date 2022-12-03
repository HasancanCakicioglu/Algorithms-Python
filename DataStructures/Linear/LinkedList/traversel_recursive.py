from model.model_characters import *

def linkedListValues(head):
    values = []
    fillValues(head, values)
    return values

def fillValues(head, values):
    if head is None: return
    values.append(head.data)
    fillValues(head.next, values)

print(linkedListValues(a))    