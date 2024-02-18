#Wyciąganie maksimum z listy

#zadanie 2b
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

#v1
def fmax(head):
    r=head.next.val
    p=head.next
    q=head
    while p!=None:
        if p.val>r:
            r=p.val
        p=p.next
    p=head.next
    while p.val!=r:
        p=p.next
        q=q.next
    q.next=p.next
    return p

#v2
def extractmax(L):
    M=L
    while L.next!=None:
        if L.next.val>M.next.val:
            M=L
        L=L.next
    R=M.next
    M.next=R.next
    R.next=None
    return R

#testy
def print_nodes(head):
    while head.next!=None:
        print(head.next.val,end=' ')
        head=head.next
    print()

head=Node(None)
a=Node(3)
b=Node(7)
c=Node(1)
head.next=a
a.next=b
b.next=c
print_nodes(head)
print(fmax(head).val)
print(extractmax(head).val)
d=Node(8)
e=Node(5)
f=Node(4)
c.next=d
d.next=e
e.next=f
print_nodes(head)
print(fmax(head).val)
print(extractmax(head).val)
