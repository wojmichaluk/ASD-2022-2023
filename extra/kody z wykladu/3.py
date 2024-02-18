from random import randint
from time import time

#operacje w kopcu
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
        
def insert(A,x):
    i=len(A)
    A.append(x)
    p=(i-1)//2
    while p>=0:
        if A[p]<A[i]:
            A[p],A[i]=A[i],A[p]
            i=p
            p=(i-1)//2
        else: break

def extract_max(A):
    a=A[0]
    l=len(A)
    A[0]=A[l-1]
    A.pop()
    heapify(A,0,l-1)
    return a

#quicksort
def QuickSort(A,p,r):
    #if p<r:
    while p<r:
        q=partition(A,p,r)
        QuickSort(A,p,q-1)
        #QuickSort(A,q+1,r)
        p=q+1

def partition(A,p,r):
    x=A[r]
    #lepszy pivot: losowy element z tablicy/
    #mediana z pierwszego, środkowego
    #i ostatniego elementu
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

#statystyki pozycyjne
def select(A,k):
    p=0
    r=len(A)-1
    q=partition(A,p,r)
    while q!=k:
        if q>k:
            r=q-1
        if q<k:
            p=q+1
        q=partition(A,p,r)
    return A[q]

#testy
T=[randint(1,1000000) for _ in range(100000)]
print(*T[:20])
R=T[::]
QuickSort(T,0,len(T)-1)
print(select(R,15))
print(*T[:20])
"""T=[randint(1,1000000) for _ in range(1000000)]
a=time()
print(select(T,15))
b=time()
print(*sorted(T)[:20],b-a)
T=[randint(1,1000000) for _ in range(5000)]
T.sort()
a=time()
print(select(T,15))
b=time()
print(*T[:20],b-a)
T=[randint(1,1000000) for _ in range(25000)]
T.sort()
a=time()
print(select(T,15))
b=time()
print(*T[:20],b-a)"""
T=[]
for i in range(10):
    insert(T,randint(1,100))
    print(*T)
for i in range(10):
    print(*T)
    print(extract_max(T)) 
