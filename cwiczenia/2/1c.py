#Implementacja MergeSort na listach jednokierunkowych
#2) scalanie

#zadanie 1c
class Node:
    def __init__(self, val):
        self.val=val
        self.next=None
        
def merge(p1,p2):
    t=Node(None)
    h=t
    p1=p1.next
    p2=p2.next
    while p1 and p2:
        if p1.val<=p2.val:
            t.next=p1
            p1=p1.next
        else:
            t.next=p2
            p2=p2.next
        t=t.next
    while p1:
        t.next=p1
        p1=p1.next
        t=t.next
    while p2:
        t.next=p2
        p2=p2.next
        t=t.next
    return h.next,t

#testy
def print_nodes(head):
    while head.next!=None:
        print(head.next.val,end=' ')
        head=head.next
    print()

head1=Node(None)
a=Node(1)
b=Node(3)
c=Node(7)
d=Node(8)
head1.next=a
a.next=b
b.next=c
c.next=d
print_nodes(head1)
head2=Node(None)
e=Node(4)
f=Node(5)
g=Node(6)
h=Node(10)
head2.next=e
e.next=f
f.next=g
g.next=h
print_nodes(head2)
i=Node(None)
i.next,j=merge(head1,head2)
print_nodes(i)
