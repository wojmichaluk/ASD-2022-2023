#QuickSort w pamięci O(logn)

from random import randint

#zadanie 1
def QuickSort(A,p,r):
    while p<r:
        q=partition(A,p,r)
        if q-p<r-q:
            QuickSort(A,p,q-1)
            p=q+1
        else:
            QuickSort(A,q+1,r)
            r=q-1

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

#testy
T=[randint(1,100) for _ in range(20)]
print(*T)
QuickSort(T,0,len(T)-1)
print(*T)
