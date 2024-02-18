#Implementacja MergeSort na listach jednokierunkowych
#3) całość

#zadanie 1d
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

def MergeSort(h):
    t=h
    while t.next!=None:
        t=t.next
    while True:
        h1=Node(None)
        h2=Node(None)
        h1.next,lt=cut(h)
        h2.next,rt=cut(h)
        if h2.next==None:
            h.next=h1.next
            return
        if t==rt:
            t=h
        mh,mt=merge(h1,h2)
        t.next=mh
        t=mt

#testy
def print_nodes(head):
    while head.next!=None:
        print(head.next.val,end=' ')
        head=head.next
    print()

head=Node(None)
a=Node(3)
b=Node(1)
c=Node(4)
d=Node(7)
e=Node(2)
f=Node(6)
g=Node(8)
h=Node(5)
head.next=a
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=g
g.next=h
print_nodes(head)
MergeSort(head)
print_nodes(head)
