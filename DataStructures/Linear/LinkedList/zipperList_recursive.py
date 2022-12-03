from model.model_numbers import *


def zipperList(head1,head2):
    if head1 == None and head2 == None: return None
    if head1 == None: return head2
    if head2 == None: return head1

    next1 = head1.next
    next2 = head2.next
    head1.next = head2
    head2.next = zipperList(next1,next2)
    return head1


print(zipperList(a,b))