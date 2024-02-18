from zad3testy import runtests
from queue import PriorityQueue

#zadanie 3

def paths(G,s,t):
    n=len(G)
    X=[float('inf') for _ in range(n)]
    Y=[float('inf') for _ in range(n)]
    Dijkstra(G,X,s)
    if X[t]==float('inf'): return 0
    Dijkstra(G,Y,t)
    E=0
    for i in range(n):
        for v,c in G[i]:
            if v>i and (X[i]+Y[v]+c==X[t] or X[v]+Y[i]+c==X[t]):
                E+=1
    return E

def Dijkstra(G,d,start):
    d[start]=0
    q=PriorityQueue()
    q.put((0,start))
    while not q.empty():
        w,u=q.get()
        if w==d[u]:
            for v,c in G[u]:
                if relax(u,d,v,c):
                    q.put((d[v],v))

def relax(u,d,v,c):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        return True
    return False	

#testy   
runtests( paths )
