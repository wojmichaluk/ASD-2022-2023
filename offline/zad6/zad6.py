#Wojciech Michaluk
#Algorytm znajduje najliczniejsze skojarzenie w grafie
#dwudzielnym nieważonym. W tym celu na podstawie
#danych wejściowych tworzony jest taki graf, gdzie
#zbiory wierzchołków to odpowiednio pracownicy i
#maszyny, krawędź oznacza, że pracownik może
#pracować na danej maszynie. Z definicji skojarzenia
#odpowiada to problemowi postawionemu w zadaniu.
#Algorytm wykorzystuje metodę Forda-Fulkersona oraz
#zmodyfikowanego BFS do znajdowania maksymalnego
#przepływu w grafie. Szacuję złożoność na O(EV), gdzie V-
#liczba wierzchołków, E-liczba krawędzi.

from zad6testy import runtests
from collections import deque

#funkcje pomocnicze
def FF(G,s,t):
    flow=0
    n=len(G)
    Gr=[[] for _ in range(n)]
    Existing_edges=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for v in G[i]:
            Gr[i].append(v)
            Gr[v].append(i)
            Existing_edges[i][v]=1
    path=BFS(Gr,s,t,Existing_edges)
    while path:
        flow+=1
        invert_edges(Existing_edges,path)
        path=BFS(Gr,s,t,Existing_edges)
    return flow

def BFS(G,s,t,E):
    n=len(G)
    par=[None for _ in range(n)]
    visited=[False for _ in range(n)]
    q=deque()
    q.append(s)
    visited[s]=True
    while q:
        v=q.pop()
        if v==t: break
        for u in G[v]:
            if E[v][u] and not visited[u]:
                par[u]=v
                visited[u]=True
                q.append(u)
    k=t
    path=[]
    while k!=None:
        path.append(k)
        k=par[k]
    if len(path)<2: return None
    path.reverse()
    return path

def invert_edges(E,path):
    for i in range(len(path)-1):
        E[path[i]][path[i+1]]=0
        E[path[i+1]][path[i]]=1

def max_association(G):
    n=len(G)
    G2=[[] for _ in range(n)]
    for i in range(n):
        for v in G[i]:
            G2[i].append(v)
    G2.append([])
    G2.append([])
    for i in range((n-1)//2):
        G2[n].append(i)
    for i in range((n-1)//2,n):
        G2[i].append(n+1)
    return FF(G2,n,n+1)

def binworker( M ):
    m=len(M)
    n=2*m+1
    G=[[] for _ in range(n)]
    for i in range(m):
        for v in M[i]:
            G[i].append(v+m)
    return max_association(G)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
