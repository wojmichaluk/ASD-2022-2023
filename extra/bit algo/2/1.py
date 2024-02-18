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

def binary_search(A,el,p,k):
    if p>k:
        return -1
    sr=(p+k)//2
    if A[sr]==el:
        return sr
    if el>A[sr]:
        return binary_search(A,el,sr+1,k)
    return binary_search(A,el,p,sr-1)

def disjunctive(A,B):
    QuickSort(A,0,len(A)-1)
    for i in range(len(B)):
        a=binary_search(A,B[i],0,len(A)-1)
        if a>=0:
            return False
    return True

#testy
m=randint(3,5)
n=randint(15,20)
T=[randint(1,100) for _ in range(m)]
A=[randint(1,100) for _ in range(n)]
print(disjunctive(T,A))
print(*T)
print(*A)
