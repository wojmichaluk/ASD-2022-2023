from queue import Queue
from queue import PriorityQueue
from math import inf

#podejście elementarne
def BFS(G,start):
    n=len(G)
    visited=[False for _ in range(n)]
    d=[-1 for _ in range(n)]
    par=[None for _ in range(n)]
    q=Queue()
    q.put((None,start,0,0))
    while not q.empty():
        t,v,w,x=q.get()
        if w>1:
            q.put((t,v,w-1,x+1))
        elif not visited[v]:
            d[v]=x
            visited[v]=True
            par[v]=t
            for u,y in G[v]:
                if not visited[u]:
                    q.put((v,u,y,d[v]+1))
    return par,d

#algorytm Dijkstry
def Dijkstra(G,start):
    n=len(G)
    d=[inf for _ in range(n)]
    par=[None for _ in range(n)]
    d[start]=0
    Q=PriorityQueue()
    for i in range(n):
        Q.put((inf,i))
    while not Q.empty():
        w,u=Q.get()
        for v,c in G[u]:
            relax(par,d,v,c,u,Q)        
    return par,d

def relax(par,d,v,c,u,Q=0):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        if Q!=0: Q.put((d[v],v))
        else: return True

#algorytm Bellmana-Forda
def Bellman_Ford(G,s):
    n=len(G)
    d=[inf]*n
    d[s]=0
    par=[None]*n
    for i in range(n-1):
        for j in range(n):
            for k in range(len(G[j])):
                relax(par,d,G[j][k][0],G[j][k][1],j)
    for j in range(n):
        for k in range(len(G[j])):
            if relax(par,d,G[j][k][0],G[j][k][1],j):
                return par,d,False
    return par,d,True

#testy
G=[[(1,2),(5,4)],[(0,2),(2,4),(5,1)],[(1,4),(3,1),(5,2)],[(2,1),(4,3)],
[(3,3),(5,1)],[(0,4),(1,1),(2,2),(4,1)]]
print(BFS(G,2))
print(Dijkstra(G,2))
print(Bellman_Ford(G,2))
G=[[(1,1),(7,2)],[(0,1),(2,3),(4,3)],[(1,3),(3,5)],[(2,5),(4,2),(6,1)],
[(1,3),(3,2),(5,3),(7,1)],[(4,3),(6,8),(8,1)],[(3,1),(5,8),(8,4)],
[(0,2),(4,1),(8,7)],[(5,1),(6,4),(7,7)]]
print(BFS(G,0))
print(Dijkstra(G,0))
print(Bellman_Ford(G,0))
G=[[(1,3)],[(2,1),(3,5)],[(0,-2),(3,7)],[(5,-5)],[(2,-3),(3,4)],[(4,2)]]
print(Bellman_Ford(G,0))
G=[[(1,3)],[(2,1),(3,5)],[(0,-2),(3,7)],[(5,-7)],[(2,-3),(3,4)],[(4,2)]]
print(Bellman_Ford(G,3))
