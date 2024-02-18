#Znajdujemy w drzewie najkrótszy korzeń
#(aby maksymalna długość - suma wag - od
#najdalszego wierzchołka była możliwie 
#najmniejsza). Pomysł: 1) Bruteforce - 
#sprawdzamy Dijkstrą z każdego wierzchołka;
#2) Przechodzimy dwukrotnie Dijkstrą.

from math import inf
from queue import PriorityQueue

#zadanie 8
def bruteforce(G):
    n=len(G)
    dists=[inf for _ in range(n)]
    for i in range(n):
        a=Dijkstra(G,i)
        max_d=a[1][0]
        for j in range(1,n):
            if a[1][j]>max_d:
                max_d=a[1][j]
        dists[i]=max_d
    min_d=dists[0]
    min_v=0
    for i in range(1,n):
        if dists[i]<min_d:
            min_d=dists[i]
            min_v=i
    return min_v
    
def longest_path(G):
    a=Dijkstra(G,0)
    n=len(G)
    max_d=a[1][0]
    max_v=0
    for i in range(1,n):
        if a[1][i]>max_d:
            max_d=a[1][i]
            max_v=i
    b=Dijkstra(G,max_v)
    max_d=b[1][0]
    max_v=0
    for i in range(1,n):
        if b[1][i]>max_d:
            max_d=b[1][i]
            max_v=i
    path=[]
    t=max_v
    while t!=None:
        path.append(t)
        t=b[0][t]
    opt=max_d/2
    min_d=max_d/2
    min_v=max_v
    for v in path:
        if abs(b[1][v]-opt)<min_d:
            min_d=abs(b[1][v]-opt)
            min_v=v
    return min_v

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
G=[[(3,11),(4,15)],[(3,17),(5,32)],[(3,41),(6,15),(7,19)],
[(0,11),(1,17),(2,41)],[(0,15),(8,32)],[(1,32)],[(2,15)],[(2,19)],[(4,32)]]
print(bruteforce(G))
print(longest_path(G))
G=[[(1,11),(2,7),(3,9)],[(0,11),(4,32),(6,41)],[(0,7),(7,8)],
[(0,9),(10,10)],[(1,32),(5,27)],[(4,27)],[(1,41)],[(2,8),(8,15),(9,13)],
[(8,15)],[(9,13)],[(3,10),(11,13),(12,12)],[(10,13),(13,17)],
[(10,12),(14,15)],[(11,17)],[(12,15)]]
print(bruteforce(G))
print(longest_path(G))
G=[[(1,22),(2,17)],[(0,22),(3,21),(4,19)],[(0,17),(5,31),(6,16)],
[(1,21)],[(1,19)],[(2,31)],[(2,16)]]
print(bruteforce(G))
print(longest_path(G))
