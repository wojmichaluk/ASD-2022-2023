from random import randint

class Node:
    def __init__(self,val=0,nex=None):
        self.val=val
        self.next=nex

def count_nodes(p):
    l=0
    while p!=None:
        l+=1
        p=p.next
    return l

def mapping(p,a):
    while p!=None:
        p.val-=a
        p=p.next

def BucketSort(p,a,b,n):
    buckets=[[] for _ in range(n+1)]
    while p!=None:
        q=p
        p=p.next
        i=int(n*q.val/(b-a))
        q.next=None
        buckets[i].append(q.val+a)
    T=[]
    for i in range(n+1):
        InsertionSort(buckets[i])
        T+=buckets[i]
    return T

def InsertionSort(T):
    n=len(T)
    for i in range(1,n):
        x=T[i]
        j=i-1
        while j>=0 and x<T[j]:
            T[j+1]=T[j]
            j-=1
        T[j+1]=x

def sort(first,a,b):
    mapping(first,a)
    n=count_nodes(first)
    T=BucketSort(first,a,b,n)
    return T

n=1000
a=100
b=150
T=[randint(100*a,100*b)/100 for _ in range(n)]
p=Node(T[0])
q=p
for i in range(1,n):
    p.next=Node(T[i])
    p=p.next
print(*T[:20])
T=sort(q,a,b)
print(*T[:20])
