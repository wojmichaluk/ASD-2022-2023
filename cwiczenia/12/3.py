#Szukamy (długości) najdłuższego rosnącego
#podciągu w tablicy A. Pomysły: O(n^2) -
#bierzemy f(i) jako długość najdłuższego
#podciągu kończącego się na A[i]. f(i) = 
#max{f(j) + 1 | A[j] < A[i]}. Można odtworzyć
#podciąg. Wersja O(nlogn): korzystamy z tego,
#że jeżeli w F będziemy trzymać wartości ostatnich
#elementów w danym podciągu, to F jest posortowana
#i zamiast drugiej pętli mamy binsearch.

from random import randint

#zadanie 3
def lis(A): #O(n^2)
    n=len(A)
    F=[1]*n
    for i in range(1,n):
        for j in range(i):
            if A[j]<A[i]:
                F[i]=max(F[i],F[j]+1)
    return max(F)

def lis2(A): #O(nlogn)
    n=len(A)
    F=[A[0]]
    for i in range(1,n):
        if A[i]>F[-1]: F.append(A[i])
        else:
            a=binsearch(F,0,len(F)-1,A[i])
            F[a]=A[i]
    return len(F)

def binsearch(A,l,p,v):
    if p<l: return l
    i=(p+l)//2
    if A[i]==v: return i
    elif A[i]>v: return binsearch(A,l,i-1,v)
    else: return binsearch(A,i+1,p,v)

#testy
A=[2,1,4,3,1,5,2,7,8,3]
print(lis(A))
print(lis2(A))
A=[1,3,5,2,4,5,3,4,6,3,5,1,3,4,6]
print(lis(A))
print(lis2(A))
A=[randint(1,10000) for _ in range(10000)]
print(lis(A))
print(lis2(A))
