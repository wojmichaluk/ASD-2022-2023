from queue import Queue
from copy import deepcopy

#znajdowanie ścieżki powiększającej (do FF)
def BFS(G,s,t):
    n=len(G)
    par=[None for _ in range(n)]
    visited=[False for _ in range(n)]
    q=Queue()
    q.put(s)
    visited[s]=True
    while not q.empty():
        v=q.get()
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

#Ford-Fulkerson
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

#pomocnicze
#do FF
def cap(G,path):
    minf=G[path[0]][path[1]]
    for i in range(1,len(path)-1):
        minf=min(minf,G[path[i]][path[i+1]])
    return minf

def update(G,path,w):
    for i in range(len(path)-1):
        G[path[i]][path[i+1]]-=w
        G[path[i+1]][path[i]]+=w

#do dwudzielnego
def bipartite(G,start_v):
    colors=[-1]*len(G)
    q=Queue()
    q.put(start_v)
    colors[start_v]=0
    while not q.empty():
        v=q.get()
        for i in range(len(G)):
            if not G[v][i]: continue
            if colors[i]==-1:
                colors[i]=(colors[v]+1)%2
                q.put(i)
            else:
                if colors[i]==colors[v]: return False
    return True,colors

#skojarzenia w grafach dwudzielnych
def max_association(G):
    a,b=bipartite(G,0)
    n=len(G)
    U=[]
    V=[]
    for i in range(n):
        if b[i]==0:
            U.append(i)
        else: V.append(i)
    G2=deepcopy(G)
    for i in range(len(V)):
        for j in range(n):
            G2[V[i]][j]=0
    G2.append([0]*(n+2))
    G2.append([0 for _ in range(n+2)])
    for i in range(n):
        G2[i].extend([0,0])
    for u in U:
        G2[n][u]=1
    for v in V:
        G2[v][n+1]=1
    return FF(G2,n,n+1)

#testy
G=[[0,4,0,3,0,0],[0,0,2,2,0,0],[0,0,0,0,0,4],
[0,0,2,2,0,0],[0,0,0,0,0,5],[0,0,0,0,0,0]]
print(FF(G,0,5))
G=[[0,10**12,10**12,0,0,0],[0,0,0,1,0,10**12],[0,0,0,0,1,10**12],
[0,0,1,0,0,0],[0,1,0,0,0,0],[0,0,0,0,0,0]]
print(FF(G,0,5))
G=[[0,0,0,0,1,0,1,0],[0,0,0,0,1,0,1,0],
[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,1],[1,1,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0],[1,1,0,1,0,0,0,0],[0,0,0,1,0,0,0,0]]
print(max_association(G))
G=[[0,0,0,0,1,1,0,0,1],[0,0,0,0,1,0,1,1,0],[0,0,0,0,0,0,1,1,1],
[0,0,0,0,0,1,1,1,1],[1,1,0,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,0],
[1,1,1,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0],[1,0,1,1,0,0,0,0,0]]
print(max_association(G))
