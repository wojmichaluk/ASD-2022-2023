#Sortowanie listy wstawianie / wybieranie

#zadanie 2c
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
def insert(head,node):
    while head.next!=None and head.next.val<node.val:
        head=head.next
    node.next=head.next
    head.next=node

def insertion_sort(head):
    T=Node(None)
    p=head.next
    while p!=None:
        insert(T,Node(p.val))
        p=p.next
    head.next=T.next

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
insertion_sort(head)
print_nodes(head)
d=Node(8)
e=Node(5)
f=Node(4)
r=head
while r.next!=None:
    r=r.next
r.next=d
d.next=e
e.next=f
print_nodes(head)
insertion_sort(head)
print_nodes(head)
