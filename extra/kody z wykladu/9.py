from math import inf
from queue import PriorityQueue

#struktura find/union
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

#Floyd-Warshall
def Floyd_Warshall(G):
    n=len(G)
    P=[[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]!=inf:
                P[i][j]=i
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if G[j][k]>G[j][i]+G[i][k]:
                    G[j][k]=G[j][i]+G[i][k]
                    P[j][k]=P[i][k]
    return G,P

#Kruskal
def Kruskal(E,n):
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
            if L[j][2]<=R[k][2]:
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
            
#Prima
def Prima(G,start):
    n=len(G)
    d=[inf for _ in range(n)]
    par=[None for _ in range(n)]
    d[start]=0
    q=PriorityQueue()
    q.put((0,start))
    while not q.empty():
        w,v=q.get()
        for u,c in G[v]:
            if c<d[u] and par[v]!=u:
                d[u]=c
                par[u]=v
                q.put((d[u],u))
    return par,d

#testy
a=Node(1)
b=Node(3)
c=Node(5)
d=Node(17)
e=Node(19)
union(a,b)
union(c,e)
print(findset(a).value)
print(findset(e).value)
union(a,c)
print(findset(b).value)
print(findset(d).value)
G=[[0,1,inf,inf,5,8],[1,0,3,inf,inf,inf],[inf,3,0,6,4,inf],
[inf,inf,6,0,2,inf],[5,inf,4,2,0,7],[8,inf,inf,inf,7,0]]
a=Floyd_Warshall(G)
print(a[0],a[1],sep='\n')
G=[[0,12,inf,11,inf,inf,inf,inf],[12,0,9,inf,inf,inf,17,inf],
[inf,9,0,7,inf,inf,inf,14],[11,inf,7,0,15,inf,inf,inf],
[inf,inf,inf,15,0,13,inf,10],[inf,inf,inf,inf,13,0,20,inf],
[inf,17,inf,inf,inf,20,0,11],[inf,inf,14,inf,10,inf,11,0]]
a=Floyd_Warshall(G)
print(a[0],a[1],sep='\n')
E=[(0,1,1),(0,4,5),(0,5,8),(1,0,1),(1,2,3),(2,1,3),(2,3,6),(2,4,4),
(3,2,6),(3,4,2),(4,0,5),(4,2,4),(4,3,2),(4,5,7),(5,0,8),(5,4,7)]
print(Kruskal(E,6))
E=[(0,1,12),(0,3,11),(1,0,12),(1,2,9),(1,6,17),(2,1,9),(2,3,7),
(2,7,14),(3,0,11),(3,2,7),(3,4,15),(4,3,15),(4,5,13),(4,7,10),
(5,4,13),(5,6,20),(6,1,17),(6,5,20),(6,7,11),(7,2,14),(7,4,10),(7,6,11)]
print(Kruskal(E,8))
G=[[(1,1),(4,5),(5,8)],[(0,1),(2,3)],[(1,3),(3,6),(4,4)],
[(2,6),(4,2)],[(0,5),(2,4),(3,2),(5,7)],[(0,8),(4,7)]]
print(Prima(G,2))
G=[[(1,12),(3,11)],[(0,12),(2,9),(6,17)],[(1,9),(3,7),(7,14)],
[(0,11),(2,7),(4,15)],[(3,15),(5,13),(7,10)],[(4,13),(6,20)],
[(1,17),(5,20),(7,11)],[(2,14),(4,10),(6,11)]]
print(Prima(G,0))
