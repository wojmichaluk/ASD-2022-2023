from random import randint

def heapify(A,i,n):
    l=2*i+1
    r=2*i+2
    min_ind=i
    if l<n and A[l]<A[min_ind]:
        min_ind=l
    if r<n and A[r]<A[min_ind]:
        min_ind=r
    if min_ind!=i:
        (A[i],A[min_ind])=(A[min_ind],A[i])
        heapify(A,min_ind,n)

def buildheap(A):
    n=len(A)
    for i in range(n//2-1,-1,-1):
        heapify(A,i,n)

def fun(T,k,x):
    A=T[::]
    buildheap(A)
    counter=0
    def wew(A,x,i=0):
        if i>=len(A) or A[i]>=x: return
        nonlocal counter
        counter+=1
        wew(A,x,2*i+1)
        wew(A,x,2*i+2)
    wew(A,x)
    return counter<k

#testy
T=[randint(1,100) for _ in range(20)]
print(*sorted(T))
x=randint(1,100)
print(x)
print(fun(T,4,x))
print(fun(T,8,x))
print(fun(T,12,x))
print(fun(T,16,x))
