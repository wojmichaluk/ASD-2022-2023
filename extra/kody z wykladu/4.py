from random import randint,uniform
from time import time 

#sortowania liniowe
def countingsort(A,k,t=-1):
    n=len(A)
    C=[0]*k
    B=[0]*n
    if t==-1:
        for i in range(n):
            C[A[i]]+=1
        for i in range(1,k):
            C[i]+=C[i-1]
        for i in range(n-1,-1,-1):
            B[C[A[i]]-1]=A[i]
            C[A[i]]-=1
        return B
    else:
        for i in range(n):
            C[ord(A[i][t])-ord('a')]+=1
        for i in range(1,k):
            C[i]+=C[i-1]
        for i in range(n-1,-1,-1):
            B[C[ord(A[i][t])-ord('a')]-1]=A[i]
            C[ord(A[i][t])-ord('a')]-=1
        return B

def radixsort(A):
    for i in range(len(A[0])):
        A=countingsort(A,ord('z')-ord('a')+1,len(A[0])-i-1)
    return A

def InsertionSort(T):
    n=len(T)
    for i in range(1,n):
        el=T[i]
        j=i-1
        while j>=0 and el<T[j]:
            T[j+1]=T[j]
            j-=1
        T[j+1]=el

def bucketsort(A):
    n=len(A)
    B=[[] for _ in range(n)]
    for i in range(n):
        B[int(n*A[i])].append(A[i])
    k=0
    for i in range(n):
        InsertionSort(B[i])
        for j in range(len(B[i])):
            A[k]=B[i][j]
            k+=1

#magiczne piątki
def magiczne_piatki(A,p,r):
    if len(A)==1: return 0
    B=[(A[p+i],p+i) for i in range(r-p+1)]
    n=(len(B)+4)//5
    medians=[0 for _ in range(n)]
    for i in range(n-1):
        medians[i]=find_median(B,5*i,5*i+5)
    medians[n-1]=find_median(B,5*(n-1),len(B))
    medians=[medians[i]+p for i in range(len(medians))]
    B=[B[i][0] for i in range(r-p+1)]
    return rek(A,medians)

def find_median(A,p,r):
    T=[(A[p+i],p+i) for i in range(r-p)]
    InsertionSort(T)
    return T[(r-p-1)//2][1]

def rek(A,med):
    if len(med)==1: return med[0]
    B=[(A[med[i]],med[i]) for i in range(len(med))]
    n=(len(med)+4)//5
    medians=[0 for _ in range(n)]
    for i in range(n-1):
        medians[i]=find_median(B,5*i,5*i+5)
    medians[n-1]=find_median(B,5*(n-1),len(B))
    medians=[med[medians[i]] for i in range(n)]
    return rek(A,medians)

def partition(A,p,r):
    index=magiczne_piatki(A,p,r)
    A[index],A[r]=A[r],A[index]
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

#testy
T=[randint(0,49) for _ in range(100)]
print(*T)
print(*countingsort(T,50))
T=["kra","art","kot","kit","ati","kil"]
T=radixsort(T)
print(*T)
T=[uniform(0,1-10e-10) for _ in range(20)]
print(*T)
bucketsort(T)
print(*T)
T=[randint(1,1000000) for _ in range(100000)]
print(*T[:20])
#a=time() 
print(select(T,15))
#b=time()
#print(*sorted(T)[:20],b-a)
print(*sorted(T)[:20])
"""T=[randint(1,1000000) for _ in range(1000000)]
T.sort()
a=time()
print(select(T,15))
b=time()
print(*T[:20],b-a)
T=[randint(1,1000000) for _ in range(5000000)]
T.sort()
a=time()
print(select(T,15))
b=time()
print(*T[:20],b-a)"""
T=[randint(1,100) for _ in range(20)]
print(*T)
print(select(T,15))
print(*sorted(T))
