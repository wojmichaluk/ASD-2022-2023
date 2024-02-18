from random import randint

def QuickSort(A,p,r):
    while p<r:
        q=partition(A,p,r)
        QuickSort(A,p,q-1)
        p=q+1

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def LowestMaxSumDivision(A):
    n=len(A)
    QuickSort(A,0,n-1)
    T=[(A[i],A[n-i-1]) for i in range(n//2)]
    return T

#testy
T=[randint(1,100) for _ in range(20)]
print(*T)
A=LowestMaxSumDivision(T)
print(*A)
