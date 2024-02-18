from random import randint

def section(T,p,q):
    select(T,0,p)
    select(T,p+1,q)
    return T[p:q+1]

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def select(A,p,k):
    r=len(A)-1
    q=partition(A,p,r)
    while q!=k:
        if q>k:
            r=q-1
        if q<k:
            p=q+1
        q=partition(A,p,r)

#testy
T=[randint(156,232) for _ in range(50)]
print(*section(T,5,15))
print(*sorted(T)[5:16])
