from random import random
from math import log

def fast_sort(tab,a):
    n=len(tab)
    for i in range(n):
        tab[i]=(tab[i],log(tab[i])/log(a))
    T=[[] for _ in range(n+1)]
    for i in range(n):
        T[int(n*tab[i][1])].append(tab[i])
    k=0
    for i in range(n+1):
        MergeSort(T[i])
        for j in range(len(T[i])):
            tab[k]=T[i][j][0]
            k+=1
    return tab

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
            if L[j][1]<=R[k][1]:
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

#testy
a=5
T=[a**random() for _ in range(25)]
T[17]=a
print(*T)
print()
print(*fast_sort(T,a))
