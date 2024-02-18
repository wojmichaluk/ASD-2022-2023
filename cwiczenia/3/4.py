#Mamy k posortowanych list - chcemy scalić je w jedną.

from random import randint

#zadanie 4
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def Merging(L):
    n=len(L)
    if n>1:
        for i in range(n//2):
            head=Node(None)
            head.next=merge(L[2*i],L[2*i+1])
            L[2*i]=head
        L=[L[2*i] for i in range((n+1)//2)]
        Merging(L)

#testy
def merge(p1,p2):
    h=t=Node(None)
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
    return h.next

def print_nodes(head):
    while head.next!=None:
        print(head.next.val,end=' ')
        head=head.next
    print()
    
k=randint(20,30)
T=[Node(None) for _ in range(k)]
for i in range(k):
    j=randint(20,30)
    A=[randint(1,100) for _ in range(j)]
    A.sort()
    N=Node(A[0])
    T[i].next=N
    M=T[i].next
    for m in range(1,j):
        M.next=Node(A[m])
        M=M.next
    print_nodes(T[i])
Merging(T)
print_nodes(T[0])
