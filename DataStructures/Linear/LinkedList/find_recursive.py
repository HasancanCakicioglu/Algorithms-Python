
from model.model_numbers import *

def linked_list_find_recursive(linked_list, value):
    if linked_list is None:
        return False
    if linked_list.val == value:
        return True
    return linked_list_find_recursive(linked_list.next, value)

print(linked_list_find_recursive(a, 3))