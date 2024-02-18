from random import randint

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
            if L[j]<=R[k]:
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

def binary_search(A,el,p,k):
    if p>k:
        return -1
    sr=(p+k)//2
    if A[sr]==el:
        return sr
    if el<A[sr]:
        return binary_search(A,el,p,sr-1)
    return binary_search(A,el,sr+1,k)

def PairsDifferingByK(A,k):
    MergeSort(A)
    counter=0
    last=A[0]-1
    for i in range(len(A)):
        a=A[i]
        if a-last!=0:
            if binary_search(A,A[i]+k,0,len(A)-1)>=0:
                counter+=1
        last=a
    return counter

#testy
T=[7,11,3,7,3,9,5]
k=4
print(PairsDifferingByK(T,k))
T=[randint(1,25) for _ in range(10)]
k=randint(2,6)
print(PairsDifferingByK(T,k))
print(*T)
print(k)
