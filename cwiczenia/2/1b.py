#Implementacja MergeSort na listach jednokierunkowych
#1) odcinanie serii naturalnych

#zadanie 1b
class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

def cut(p):
    q=p
    q=q.next
    if q==None:
        return None,None
    while q.next!=None and q.val<=q.next.val:
        q=q.next
    w=p.next
    p.next=q.next
    q.next=None
    return w,q

#testy
def print_nodes(head):
    while head.next!=None:
        print(head.next.val,end=' ')
        head=head.next
    print()

head=Node(None)
a=Node(3)
b=Node(7)
c=Node(8)
d=Node(1)
e=Node(5)
f=Node(4)
head.next=a
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
print_nodes(head)
g,h=cut(head)
i=Node(None)
i.next=g
print_nodes(i)
print_nodes(head)
