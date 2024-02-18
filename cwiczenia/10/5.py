#Szukanie maksymalnej liczby ścieżek
#z s do t rozłącznych wierzchołkowo:
#Pomysł - każdy wierzchołek rozdwajamy,
#1) wszystkie wychodzące, 2) wszystkie
#wchodzące, parę łączymy krawędzią "kontrolną"
#1. Następnie używamy Forda - Fulkersona.

from queue import Queue
from copy import deepcopy

#funkcje pomocnicze
def FF(G,s,t):
    flow=0
    Gr=deepcopy(G)
    paths=[]
    path=BFS(Gr,s,t)
    while path:
        paths.append(path)
        w=cap(Gr,path)
        flow+=w
        update(Gr,path,w)
        path=BFS(Gr,s,t)
    return flow,paths

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

#zadanie 5
def max_no_paths(G,s,t):
    n=len(G)
    G2=[[0 for _ in range(2*n-2)] for _ in range(2*n-2)]
    mod=0
    for i in range(n):
        if i==s or i==t:
            mod+=1
            for j in range(n):
                if G[i][j]: G2[i][j]=1
        else:
            for j in range(n):
                if G[i][j]: G2[i][j]=1
                if G[j][i]: G2[i+n-mod][j]=1
                #if G[j][i]: G2[j][i+n-mod]=1
            G2[i+n-mod][i]=1
    return FF(G2,s,t)

#próba "naiwnego" poprawienia
def correction(G,s,t):
    flow,paths=max_no_paths(G,s,t)
    new_flow=flow
    used_vertices=[False for _ in range(len(G))]
    for i in range(flow):
        flag=True
        for j in range(1,len(paths[i])-1):
            if used_vertices[paths[i][j]]:
                flag=False
                new_flow-=1
                break
        if flag:
            print(paths[i])
            for j in range(1,len(paths[i])-1):
                used_vertices[paths[i][j]]=True
    return new_flow

#testy
G=[[0,1,1,0],[0,0,0,1],[0,1,0,0],[0,0,1,0]]
#print(max_no_paths(G,0,2))
print(correction(G,0,2))
G=[[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]]
#print(max_no_paths(G,0,2))
print(correction(G,0,2))
G=[[0,1,1,1,0,1],[0,0,0,1,0,1],[0,0,0,0,1,1],
[0,0,0,0,1,1],[0,0,0,0,0,1],[0,0,0,0,0,0]]
#print(max_no_paths(G,0,5))
print(correction(G,0,5))
G=[[0,1,1,1,0,1],[1,0,0,1,0,1],[1,0,0,0,1,1],
[1,1,0,0,1,1],[0,0,1,1,0,1],[1,1,1,1,1,0]]
#print(max_no_paths(G,0,5))
print(correction(G,0,5))
#ale dla tych nie działało...
G=[[0,1,0,1,0],[0,0,1,0,1],[0,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0]]
#print(max_no_paths(G,0,2))
print(correction(G,0,2))
G=[[0,1,0,1,0],[1,0,1,1,1],[0,1,0,0,1],[1,1,0,0,0],[0,1,1,0,0]]
#print(max_no_paths(G,0,2))
print(correction(G,0,2))
