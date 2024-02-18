#Przewodnik turystyczny, ale bez DFS ani
#BFS. Chcemy znaleźć maksymalną przepustowość.
#Pomysł: używamy Kruskala, ale znajdujemy 
#"maksymalne" drzewo rozpinające, aż nie 
#połączą się wierzchołki s i t. 

from math import inf
from math import ceil
from queue import PriorityQueue

#funkcje pomocnicze
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
    MergeSort(E)
    V=[Node(i) for i in range(n)]
    for e in E:
        u,v,w=e
        if findset(V[u])!=findset(V[v]):
            union(V[u],V[v])
            A+=[e]
    return A

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
            if L[j][2]>=R[k][2]:
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

def Dijkstra(G,start):
    n=len(G)
    d=[inf for _ in range(n)]
    par=[None for _ in range(n)]
    d[start]=0
    Q=PriorityQueue()
    Q.put((0,start))
    while not Q.empty():
        w,u=Q.get()
        if w==d[u]:
            for v,c in G[u]:
                if relax(par,d,v,c,u):
                    Q.put((d[v],v))
    return par,d

def relax(par,d,v,c,u):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

#zadanie 5
def Transport(E,s,k,n,m):
    E=kruskal(E,m)
    G=[[] for _ in range(m)]
    for e in E:
        G[e[0]].append((e[1],e[2]))
        G[e[1]].append((e[0],e[2]))
    par,d=Dijkstra(G,s)
    path=[]
    t=k
    while t!=None:
        path.append(t)
        t=par[t]
    path.reverse()
    mini=d[path[1]]-d[path[0]]
    for i in range(1,len(path)-1):
        a=d[path[i+1]]-d[path[i]]
        if mini>a: mini=a
    return path,mini,ceil(n/mini)

#testy
E=[(0,1,25),(0,2,50),(1,0,25),(1,2,10),(1,3,50),(2,0,50),(2,1,10),
(2,3,20),(3,1,50),(3,2,20),(3,4,9),(3,5,7),(3,6,15),(4,3,9),(4,5,11),
(4,6,14),(5,3,7),(5,4,11),(5,6,10),(6,3,15),(6,4,14),(6,5,10)]
print(Transport(E,0,5,100,7))
E=[(0,1,17),(0,2,31),(0,3,11),(1,0,17),(1,2,19),(1,3,25),
(2,0,31),(2,1,19),(2,4,15),(3,0,11),(3,1,25),(3,4,13),
(3,5,7),(4,2,15),(4,3,13),(4,5,14),(5,3,7),(5,4,14)]
print(Transport(E,0,5,300,6))
E=[(0,1,12),(0,2,12),(0,3,10),(1,0,12),(1,2,8),(1,4,15),(2,0,12),(2,1,8),
(2,3,4),(2,4,7),(3,0,10),(3,2,4),(3,4,11),(4,1,15),(4,2,7),(4,3,11)]
print(Transport(E,3,2,50,5))
E=[(0,1,10),(0,2,12),(1,0,10),(1,2,9),(1,3,18),(2,0,12),(2,1,9),
(2,4,7),(2,5,16),(3,1,18),(3,4,13),(3,6,15),(4,2,7),(4,3,13),
(4,6,11),(5,2,16),(5,6,6),(6,3,15),(6,4,11),(6,5,6)]
print(Transport(E,0,6,100,7))
