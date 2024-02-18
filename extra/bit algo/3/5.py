class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def SortH(p,k):
    n=0
    q=p
    while q:
        q=q.next
        n+=1
    k=min(k,n-1)
    T=[]
    q=r=p
    for i in range(k+1):
        T.append(r.val)
        r=r.next
    buildheap(T)
    for i in range(n-k-1):
        q.val=extract_min(T)
        insert(T,r.val)
        r=r.next
        q=q.next
    for i in range(k+1):
        q.val=extract_min(T)
        q=q.next
    return p

def buildheap(A):
    n=len(A)
    for i in range(n//2-1,-1,-1):
        heapify_min(A,i,n)
    
def insert(T,x):
    l=len(T)
    T.append(x)
    heapify_min_up(T,l)

def heapify_min(A,i,n):
    l=2*i+1
    r=2*i+2
    min_ind=i
    if l<n and A[l]<A[min_ind]:
        min_ind=l
    if r<n and A[r]<A[min_ind]:
        min_ind=r
    if min_ind!=i:
        (A[i],A[min_ind])=(A[min_ind],A[i])
        heapify_min(A,min_ind,n)

def heapify_min_up(A,i):
    p=(i-1)//2
    if p>=0:
        if A[p]>A[i]:
            A[p],A[i]=A[i],A[p]
            heapify_min_up(A,p)

def extract_min(T):
    a=T[0]
    l=len(T)
    T[0],T[l-1]=T[l-1],T[0]
    T.pop()
    heapify_min(T,0,l-1)
    return a

#testy
def print_nodes(p):
    while p:
        print(p.val,end=' ')
        p=p.next
    print()

p=Node(6)
a=Node(5)
b=Node(3)
c=Node(2)
d=Node(8)
e=Node(10)
f=Node(9)
p.next=a
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
print_nodes(p)
p=SortH(p,3)
print_nodes(p)  
