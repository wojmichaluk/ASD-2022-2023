#Sortowanie tablicy n liczb, w której występuje O(logn)
#różnych wartości. Oczekiwana złożoność O(nlog(logn)).
#Pomysł: przepisujemy dane do tablicy T, jeżeli wcześniej
#wartości nie było - dodajemy krotkę z wartością i liczbą
#wystąpień=1, jeżeli była - zwiększamy liczbę wystąpien o 1.

from random import randint
from math import log2

#zadanie 2
def Sort(A):
    n=len(A)
    T=[]
    for i in range(n):
        a=binary_search(T,A[i],0,len(T)-1)
        if a[0]: T[a[1]]=(T[a[1]][0],T[a[1]][1]+1)
        else: T=T[:a[1]]+[(A[i],1)]+T[a[1]:]
    m=0
    for j in range(len(T)):
        for k in range(T[j][1]):
            A[m]=T[j][0]
            m+=1

def binary_search(A,el,p,r):
    mid=(p+r)//2
    if p>r: return (False,mid+1)
    if A[mid][0]==el: return (True,mid)
    if A[mid][0]>el: return binary_search(A,el,p,mid-1)
    return binary_search(A,el,mid+1,r)

#testy
T=[0,2,1,2,0,0,1,2]
Sort(T)
print(*T)
n=1000000
k=randint(1,100)
T=[randint(0,int(k*log2(n))) for _ in range(n)]
tab=sorted(T)
Sort(T)
print(tab==T)
