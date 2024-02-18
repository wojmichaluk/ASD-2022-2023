from random import randint

#sortowanie przez scalanie
def MergeSort(A):
    n=len(A)
    if n>1:
        i=n//2
        L=A[:i]
        R=A[i:]
        MergeSort(L)
        MergeSort(R)
        j=k=0
        while j<i and k<n-i:
            if L[j]<R[k]:
                A[j+k]=L[j]
                j+=1
            else:
                A[j+k]=R[k]
                k+=1
        while j<i:
            A[j+k]=L[j]
            j+=1
        while k<n-i:
            A[j+k]=R[k]
            k+=1

#sortowanie kopcowe
def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapify(A,i,n):
    l=left(i)
    r=right(i)
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
    for i in range(parent(n-1),-1,-1):
        heapify(A,i,n)

def heapsort(A):
    n=len(A)
    buildheap(A)
    for i in range(n-1,0,-1):
        (A[0],A[i])=(A[i],A[0])
        heapify(A,0,i)

#testy
T1=[randint(1,100) for _  in range(20)]
T2=T1[::]
print(*T1)
heapsort(T1)
MergeSort(T2)
print(*T1)
print(*T2)
