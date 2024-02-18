#Transport atomowy - chcemy stwierdzić, czy
#istnieje droga, tak żeby osoba 1. przeszła
#z s do t, a 2. z t do s, przy czym nie mogą
#być zbyt blisko siebie (odległość większa niż d).
#Pomysł: 1) Floyd - Warshall dla całego grafu.
#2) Tworzymy nowy graf z wierzchołkami (u,v)
#(rozdzielonych na (u',v) i (u,v')), dla których
#w oryginalnym grafie odległośc >d. Szukamy ścieżki
#z (s,t) do (t,s).

from queue import Queue
from math import inf

#pomocnicze funkcje
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

def BFS(G,s):
    q=Queue()
    n=len(G)
    visited=[False for _ in range(n)]
    d=[-1 for _ in range(n)]
    parent=[None for _ in range(n)]
    d[s]=0
    visited[s]=True
    q.put(s)
    while not q.empty():
        v=q.get()
        for u in G[v]:
            if not visited[u]:
                d[u]=d[v]+1
                parent[u]=v
                visited[u]=True
                q.put(u)
    return d,parent,visited

#zadanie 6
def nuclear_transport(G,s,t,d):
    n=len(G)
    Gr=[[G[i][j] for j in range(n)] for i in range(n)]
    G,P=Floyd_Warshall(G)
    new_G=[[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]!=inf and G[i][j]>d:
                new_G[i][j]=True
    if not G[s][t]: return False
    Graph=[[] for _ in range(n*n)]
    for i in range(n):
        for j in range(n):
            if new_G[i][j]:
                for k in range(n):
                    if k!=j and new_G[i][k] and Gr[j][k]!=inf:
                        Graph[n*i+j].append(n*i+k)
                for k in range(n):
                    if k!=i and new_G[k][j] and Gr[i][k]!=inf:
                        Graph[n*i+j].append(n*k+j)
    d,par,vis=BFS(Graph,n*s+t)
    k=n*t+s
    path=[]
    while k!=None:
        path.append((k//n,k%n))
        k=par[k]
    path.reverse()
    if path[0]!=(s,t): return False
    return True,path

#testy
G=[[0,7,5,inf,inf,inf],[7,0,8,3,6,inf],[5,8,0,inf,10,inf],
[inf,3,inf,0,inf,12],[inf,6,10,inf,0,7],[inf,inf,inf,12,7,0]]
print(nuclear_transport(G,0,5,7))
G=[[0,8,8,inf],[8,0,2,6],[8,2,0,5],[inf,6,5,0]]
print(nuclear_transport(G,0,3,3))
G=[[0,7,inf,inf,11],[7,0,4,10,inf],[inf,4,0,6,5],[inf,10,6,0,10],[11,inf,5,10,0]]
print(nuclear_transport(G,0,3,5))
G=[[0,7,5,inf,inf,inf,inf],[7,0,4,inf,inf,inf,inf],[5,4,0,inf,inf,inf,inf],
[inf,inf,inf,0,10,6,7],[inf,inf,inf,10,0,12,inf],
[inf,inf,inf,6,12,0,9],[inf,inf,inf,7,inf,9,0]]
print(nuclear_transport(G,0,4,1))
