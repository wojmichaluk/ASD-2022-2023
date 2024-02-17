#Wojciech Michaluk
#Algorytm najpierw zamienia słowa na tablicę,
#która przechowuje liczbę poszczególnych liter
#dla każdego słowa. Następnie wykonuje sortowanie
#pozycyjne (dla każdej z liter), żeby anagramy
#znajdowały się na sąsiednich pozycjach w tablicy,
#później szuka najdłuższej identycznej serii w tablicy.
#Szacuję złożoność czasową algorytmu na O(N) -
#wykorzystanie sortowań radixsort i countingsort,
#złożoność pamięciowa to też O(N) - countingsort.

from kol1btesty import runtests

def f(T):
    n=len(T)
    for i in range(n):
        T[i]=Letters(T[i])
    RadixSort(T)
    maxi=curr=1
    for i in range(1,n):
        if T[i]==T[i-1]: curr+=1
        else:
            if curr>maxi: maxi=curr
            curr=1
    if curr>maxi: maxi=curr
    return maxi

def RadixSort(A):
    k=ord('z')-ord('a')+1
    n=len(A)
    for i in range(k-1,-1,-1):
        maxi=A[0][i]
        for j in range(1,n):
            if A[j][i]>maxi: maxi=A[j][i]
        CountingSort(A,maxi+1,i)
            
def CountingSort(A,k,ind):
    n=len(A)
    C=[0]*k
    B=[0]*n
    for i in range(n):
        C[A[i][ind]]+=1
    for i in range(1,k):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i][ind]]-1]=A[i]
        C[A[i][ind]]-=1
    for i in range(n): A[i]=B[i]

def Letters(T):
    k=ord('z')-ord('a')+1
    n=len(T)
    C=[0]*k
    for i in range(n):
        C[ord(T[i])-ord('a')]+=1
    return C

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
#wzorcowy próg złożoności
runtests( f, all_tests=True )
