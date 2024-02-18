#Zaimplementuj algorytm Dijkstry.

from math import inf
from queue import PriorityQueue

#zadanie 1
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

#testy
G=[[(1,2),(5,4)],[(0,2),(2,4),(5,1)],[(1,4),(3,1),(5,2)],[(2,1),(4,3)],
[(3,3),(5,1)],[(0,4),(1,1),(2,2),(4,1)]]
print(Dijkstra(G,2))
G=[[(1,1),(7,2)],[(0,1),(2,3),(4,3)],[(1,3),(3,5)],[(2,5),(4,2),(6,1)],
[(1,3),(3,2),(5,3),(7,1)],[(4,3),(6,8),(8,1)],[(3,1),(5,8),(8,4)],
[(0,2),(4,1),(8,7)],[(5,1),(6,4),(7,7)]]
print(Dijkstra(G,0))

