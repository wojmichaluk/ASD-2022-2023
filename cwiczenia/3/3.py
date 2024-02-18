#Wstawianie do kopca binarnego

from random import randint

#zadanie 3
class Heap:
    def __init__(self,n):
        self.T=[0]*n
        self.size=0

def insert(H,x):
    i=H.size
    p=(H.size-1)//2
    H.T[H.size]=x
    H.size+=1
    while p>=0:
        if H.T[p]<H.T[i]:
            H.T[p],H.T[i]=H.T[i],H.T[p]
        else: return
        i=p
        p=(p-1)//2

#testy
def heapify(A,i,n):
    l=2*i+1
    r=2*i+2
    max_ind=i
    if l<n and A[l]>A[max_ind]:
        max_ind=l
    if r<n and A[r]>A[max_ind]:
        max_ind=r
    if max_ind!=i:
        (A[i],A[max_ind])=(A[max_ind],A[i])
        heapify(A,max_ind,n)

def buildheap(A):
    n=len(A)
    for i in range((n-1)//2,-1,-1):
        heapify(A,i,n)
        
T=[randint(1,100) for _ in range(20)]
buildheap(T)
print(*T)
H=Heap(21)
H.T[:20]=T
H.size=20
insert(H,70)
T=H.T
print(*T)
