from model.model_characters import *


def linkedListTraversel(head):
    current = head
    while head is not None:
        print(head.data)
        head = head.next

linkedListTraversel(a)