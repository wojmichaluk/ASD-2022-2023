from math import inf
from queue import PriorityQueue

#zadanie 5
def Dijkstra(G,start):
    n=len(G)
    d=[inf for _ in range(n)]
    edges=[inf for _ in range(n)]
    par=[None for _ in range(n)]
    d[start]=0
    edges[start]=0
    Q=PriorityQueue()
    Q.put((0,start,0))
    while not Q.empty():
        w,u,e=Q.get()
        if w==d[u]:
            for v,c in G[u]:
                if relax(par,d,v,c,u,edges,e+1):
                    Q.put((d[v],v,e+1))
    return par,d

def relax(par,d,v,c,u,edges,e):
    if d[v]>d[u]+c or (d[v]==d[u]+c and edges[v]>e):
        d[v]=d[u]+c
        par[v]=u
        edges[v]=e
        return True
    return False

def the_bestest_paths(G,start):
    par,d=Dijkstra(G,start)
    n=len(G)
    for i in range(n):
        if i!=start:
            print(start,"->",i,"length:",d[i],end='\t')
            print_path(par,start,i)
    print()

def print_path(parent,start,u):
    T=[]
    while u!=None:
        T.append(u)
        u=parent[u]
    for i in range(len(T)-1,-1,-1):
        print(T[i],end='')
    print()
    
#testy
G=[[(1,5),(3,13),(4,12)],[(0,5),(2,7),(3,6)],[(1,7),(3,2)],
[(0,13),(1,6),(2,2),(4,1)],[(0,12),(3,1)]]
the_bestest_paths(G,0)
G=[[(1,11),(2,7)],[(0,11),(2,3),(3,2),(4,7)],[(0,7),(1,3),(3,7),
(5,6)],[(1,2),(2,7),(4,5)],[(1,7),(3,5),(5,10)],[(2,6),(4,10)]]
the_bestest_paths(G,2)
G=[[(1,2),(2,5)],[(0,2),(2,3)],[(0,5),(1,3),
(3,4),(4,7)],[(2,4),(4,3)],[(2,7),(3,3)]]
the_bestest_paths(G,1)
