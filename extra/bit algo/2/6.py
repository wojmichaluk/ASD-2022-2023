from random import randint

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

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

def EuclideanDistance(A):
    n=len(A)
    if n%2==1:
        suma=0
        a=select(A,n//2)
        for i in range(n):
            suma+=abs(a-A[i])
        return a,suma
    else:
        suma=sumb=0
        a=select(A,(n-1)//2)
        b=select(A,(n+1)//2)
        for i in range(n):
            suma+=abs(a-A[i])
            sumb+=abs(b-A[i])
        if a<=b:
            return a,suma
        return b,sumb

#testy
T=[randint(1,20) for _ in range(12)]
print(*T)
print(EuclideanDistance(T))
