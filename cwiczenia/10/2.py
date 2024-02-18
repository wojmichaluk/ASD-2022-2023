#Wiele źródeł i wiele ujść. Pomysł:
#tworzymy nowe wierzchołki s i t, łączymy
#s z każdym ze źródeł, t z każdym z ujść.
#Na krawędziach wagi mogą być nieskończoność.
#Szukamy przepływu z s do t.

from queue import Queue
from copy import deepcopy

#funkcje z zadania 1
def FF(G,s,t):
    flow=0
    Gr=deepcopy(G)
    path=BFS(Gr,s,t)
    while path:
        w=cap(Gr,path)
        flow+=w
        update(Gr,path,w)
        path=BFS(Gr,s,t)
    return flow

def BFS(G,s,t):
    n=len(G)
    par=[None for _ in range(n)]
    visited=[False for _ in range(n)]
    q=Queue()
    q.put(s)
    visited[s]=True
    while not q.empty():
        v=q.get()
        if v==t: break
        for i in range(n):
            if G[v][i]>0 and not visited[i]:
                par[i]=v
                visited[i]=True
                q.put(i)
    k=t
    path=[]
    while k!=None:
        path.append(k)
        k=par[k]
    if len(path)<2: return None
    path.reverse()
    return path

def cap(G,path):
    minf=G[path[0]][path[1]]
    for i in range(1,len(path)-1):
        minf=min(minf,G[path[i]][path[i+1]])
    return minf

def update(G,path,w):
    for i in range(len(path)-1):
        G[path[i]][path[i+1]]-=w
        G[path[i+1]][path[i]]+=w

#zadanie 2
def multiFF(G,sources,sinks):
    n=len(G)
    G2=deepcopy(G)
    G2.append([0]*(n+2))
    G2.append([0 for _ in range(n+2)])
    for i in range(n):
        G2[i].extend([0,0])
    for u,v in sources:
        G2[n][u]=v
    for u,v in sinks:
        G2[u][n+1]=v
    return FF(G2,n,n+1)

#testy
G=[[0,0,7,15,12,0,0,0],[0,0,0,7,9,0,0,0],
[7,0,0,0,3,11,0,0],[15,7,0,0,0,0,13,12],
[12,9,3,0,0,4,0,0],[0,0,11,0,4,0,0,0],
[0,0,0,13,0,0,0,0],[0,0,0,12,0,0,0,0]]
sources=[(0,50),(1,30)]
sinks=[(5,max(FF(G,0,5),FF(G,1,5))),(6,max(FF(G,0,6),FF(G,1,6))),(7,max(FF(G,0,7),FF(G,1,7)))]
print(multiFF(G,sources,sinks))
G=[[0,3,0,4,5,0],[3,0,0,10,0,9],[0,0,0,7,0,2],
[4,10,7,0,0,0],[5,0,0,0,0,4],[0,9,2,0,4,0]]
sources=[(0,6),(2,10)]
sinks=[(5,max(FF(G,0,5),FF(G,2,5)))]
print(multiFF(G,sources,sinks))
G=[[0,0,15,12,0,0,0],[0,0,25,7,0,0,0],[15,25,0,0,0,0,0],
[12,7,0,0,0,11,12],[0,0,0,0,0,20,4],
[0,0,0,11,20,0,0],[0,0,0,12,4,0,0]]
sources=[(0,30),(5,25)]
sinks=[(1,max(FF(G,0,1),FF(G,5,1))),(6,max(FF(G,0,6),FF(G,5,6)))]
print(multiFF(G,sources,sinks))
