#Implementacja Forda - Fulkersona. Pomysł:
#dla każdej istniejącej krawędzi dokładamy
#krawędź przeciwną o wadze 0. Po znalezieniu
#przepływu (po wagach >0) pierwotne krawędzie
#pomniejszamy o jego wartość, a powrotne zwiększamy.
#Następnie szukamy kolejnej ścieżki powiększającej itd.

from queue import Queue
from copy import deepcopy

#zadanie 1
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
        
#testy
#skierowane
G=[[0,50,3,0,0],[0,0,7,20,0],
[0,0,0,10,3],[0,0,0,0,9],[0,0,0,0,0]]
print(FF(G,0,4))
G=[[0,12,0,0,0,0,9],[0,0,5,0,6,0,0],[7,0,0,10,0,0,11],
[0,12,10,0,0,0,14],[0,0,0,0,0,7,0],
[0,0,0,4,0,0,0],[0,0,0,0,0,0,0]]
print(FF(G,1,6))
G=[[0,14,0,3],[0,0,5,6],[0,0,0,0],[0,0,12,0]]
print(FF(G,0,2))
#nieskierowany
G=[[0,2,0,5],[2,0,3,0],[0,3,0,7],[5,0,7,0]]
print(FF(G,0,2))
G=[[0,0,15,2,10],[0,0,8,7,0],
[15,8,0,0,3],[2,7,0,0,0],[10,0,3,0,0]]
print(FF(G,0,3))
G=[[0,10,12,0,0,0],[10,0,0,0,5,5],[12,0,0,4,0,0],
[0,0,4,0,0,10],[0,5,0,0,0,7],[0,5,0,10,7,0]]
print(FF(G,0,5))
