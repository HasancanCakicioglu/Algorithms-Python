from model.model_numbers import *

def zipperLists(head1,head2):
    tail = head1
    current1 = head1.next
    current2 = head2
    count = 0

    while(current1 != None and current2 !=None):
        if(count % 2 == 0):
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        count += 1

    if current1 != None:
        tail.next = current1
    if current2 != None:
        tail.next = current2
    return head1         

print(zipperLists(a,b))    