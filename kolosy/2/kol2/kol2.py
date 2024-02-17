#Wojciech Michaluk
#Algorytm najpierw buduje reprezentację grafu
#w postaci listy krawędzi. Następnie je sortuje oraz
#każdej krawędzi przypisuje indeks. Wykorzystując
#algorytm Kruskala i strukturę find/union, wyznacza
#MST dla podzbioru krawędzi, pomijając pewną ich
#liczbę od początku tak, aby krawędzie w MST
#potencjalnie mogły mieć bezpośrednie kolejne
#indeksy (wtedy drzewo jest piękne). Szacuję
#złożoność czasową algorytmu na O(VElog*E),
#a złożoność pamięciową na O(VE).

from kol2testy import runtests

def beautree(G):
    F=[]
    n=len(G)
    for i in range(n):
        for j,w in G[i]:
            F.append((w,i,j))
    F.sort()
    k=len(F)//2
    E=[]
    for i in range(k):
        E.append(F[2*i])
    for i in range(k):
        E[i]=(E[i][0],E[i][1],E[i][2],i)
    i=0
    while i<k-n+2:
        A=kruskal(E[i:],n)
        if A and A[-1][1]-A[0][1]==n-2:
            break
        if not A: return None
        i=A[-1][1]-n+2    
    suma=A[0][0]
    for i in range(1,n-1):
        suma+=A[i][0]
    return suma

class Node:
    def __init__(self,value):
        self.parent=self
        self.rank=0
        self.value=value

def findset(x):
    if x.parent!=x:
        x.parent=findset(x.parent)
    return x.parent

def union(x,y):
    x=findset(x)
    y=findset(y)
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1

def kruskal(E,n):
    A=[]
    V=[Node(i) for i in range(n)]
    for e in E:
        w,i,j,x=e
        if findset(V[i])!=findset(V[j]):
            union(V[i],V[j])
            A.append((w,x))
    if len(A)<n-1:
        return None
    return A

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
