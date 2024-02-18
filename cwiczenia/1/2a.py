#Wstawianie do posortowanej listy

#zadanie 2a
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
def insert(head,node):
    """
    #niepotrzebne
    if head.next==None:
        head.next=node
        return
    """
    while head.next!=None and head.next.val<node.val:
        head=head.next
    node.next=head.next
    head.next=node

#testy
def print_nodes(head):
    while head.next!=None:
        print(head.next.val,end=' ')
        head=head.next
    print()

head=Node(None)
insert(head,Node(7))
insert(head,Node(3))
print_nodes(head)
insert(head,Node(6))
insert(head,Node(9))
print_nodes(head)
insert(head,Node(1))
insert(head,Node(5))
print_nodes(head)
