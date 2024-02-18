#Spójność krawędziowa - ile krawędzi trzeba usunąć,
#żeby graf przestał być spójny. Graf nieważony -
#krawędzie mają wagę 1. Pomysł dla grafu nieskierowanego:
#szukamy min_cut (liczymy maksymalny przepływ do każdego
#z wierzchołków), wybieramy z tego minimum (min. liczbę
#krawędzi wychodzących z s). Jeżeli chcemy znaleźć
#krawędzie dla każdego ujścia, wybieramy dowolne ujście
#z minimum.

from queue import Queue
from copy import deepcopy
from copy import copy

#funkcje pomocnicze
def FF(G,s,t):
    flow=0
    Gr=deepcopy(G)
    paths=[]
    path=BFS(Gr,s,t)
    while path:
        #graf nieważony
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

#zadanie 3
#nieskierowany
def edge_coherence(G,s):
    n=len(G)
    flows=[n-1 for _ in range(n)]
    paths=[[] for _ in range(n)]
    for i in range(n):
        if i!=s:
            flows[i],path=FF(G,s,i)
            paths[i]=copy(path)
    mini=flows[0]
    min_path=paths[0]
    for i in range(1,n):
        if flows[i]<mini:
            mini=flows[i]
            min_path=paths[i]
        elif flows[i]==mini:
            flag=1
            for j in range(mini):
                if len(paths[i][j])>len(min_path[j]):
                    flag=0
                    break
            if flag: min_path=paths[i]
    for i in range(mini):
        min_path[i]=min_path[i][len(min_path[i])-2:]
    return mini,min_path

#skierowany
def dir_edge_coherence(G):
    n=len(G)
    flows=[n-1 for _ in range(n)]
    paths=[[] for _ in range(n)]
    for i in range(n):
        mini_v=n-1
        for j in range(n):
            if i!=j:
                mini_v,path=FF(G,j,i)
                if flows[i]>mini_v:
                    flows[i]=mini_v
                    paths[i]=copy(path)
    mini=flows[0]
    min_path=paths[0]
    for i in range(1,n):
        if flows[i]<mini:
            mini=flows[i]
            min_path=paths[i]
        elif flows[i]==mini:
            flag=1
            for j in range(mini):
                if len(paths[i][j])>len(min_path[j]):
                    flag=0
                    break
            if flag: min_path=paths[i]
    for i in range(mini):
        min_path[i]=min_path[i][len(min_path[i])-2:]
    return mini,min_path

#testy
G=[[0,1,0,1,1,0],[1,0,0,1,0,0],[0,0,0,1,1,1],
[1,1,1,0,1,0],[1,0,1,1,0,1],[0,0,1,0,1,0]]
print(edge_coherence(G,0))
G=[[0,1,0,0,0,0],[0,0,1,1,0,0],[0,0,0,1,0,1],
[1,0,0,0,1,0],[1,0,1,0,0,0],[0,0,0,0,1,0]]
print(dir_edge_coherence(G))
G=[[0,1,0,1,0],[1,0,1,1,1],
[0,1,0,0,1],[1,1,0,0,1],[0,1,1,1,0]]
print(edge_coherence(G,1))
G=[[0,1,0,1,0],[0,0,0,1,1],
[0,1,0,0,0],[0,0,0,0,0],[0,0,1,1,0]]
print(dir_edge_coherence(G))
G=[[0,1,1,0,0,0],[1,0,1,1,0,0],[1,1,0,0,0,0],
[0,1,0,0,1,1],[0,0,0,1,0,1],[0,0,0,1,1,0]]
print(edge_coherence(G,4))
G=[[0,0,1,0,0,0],[1,0,0,1,0,0],[0,1,0,0,0,0],
[0,1,0,0,1,0],[0,0,0,0,0,1],[0,0,0,1,0,0]]
print(dir_edge_coherence(G))
