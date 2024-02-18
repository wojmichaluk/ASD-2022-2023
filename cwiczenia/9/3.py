#Dla grafu wazonego G oblicz wagę cyklu o 
#minimalnej wadze. Pomysł: klasyczny Floyd-
#Warshall, ale ustalamy odległość wierzchołka
#od samego siebie na nieskończoność, później
#szukamy minimum na przekątnej głównej. 

from math import inf
from queue import PriorityQueue

#zadanie 3
#skierowany
def Floyd_Warshall(G):
    n=len(G)
    P=[[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]!=inf:
                P[i][j]=i
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if G[j][k]>G[j][i]+G[i][k]:
                    G[j][k]=G[j][i]+G[i][k]
                    P[j][k]=P[i][k]
    mini=G[0][0]
    for i in range(1,n):
        if mini>G[i][i]:
            mini=G[i][i]
    #return G,P,mini
    if mini==inf: return "no cycle"
    return mini

#nieskierowany
def not_directed(G):
    n=len(G)
    mini=Dijkstra(G,0)
    for i in range(1,n):
        a=Dijkstra(G,i)
        if a<mini: mini=a
    if mini==inf: return "no cycle"
    return mini

def Dijkstra(G,start):
    n=len(G)
    d=[inf for _ in range(n)]
    par=[None for _ in range(n)]
    Q=PriorityQueue()
    if len(G[start])==0: return d[start]
    d[G[start][0][0]]=G[start][0][1]
    par[G[start][0][0]]=start
    Q.put((G[start][0][1],G[start][0][0]))
    while not Q.empty():
        w,u=Q.get()
        if w==d[u]:
            for v,c in G[u]:
                if par[u]!=v and relax(par,d,v,c,u):
                    Q.put((d[v],v))
    return d[start]

def relax(par,d,v,c,u):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

#testy
G=[[inf,2,inf,inf,inf,inf],[inf,inf,3,inf,1,inf],[inf,inf,inf,1,inf,inf],
[2,5,inf,inf,inf,inf],[inf,inf,inf,inf,inf,4],[inf,7,inf,inf,inf,inf]]
print(Floyd_Warshall(G))
G=[[inf,7,inf,1],[2,inf,2,inf],[7,inf,inf,3],[inf,3,6,inf]]
print(Floyd_Warshall(G))
G=[[inf,3,inf,inf,inf,inf],[inf,inf,7,inf,inf,inf],[inf,inf,inf,5,inf,inf],
[inf,inf,inf,inf,11,17],[inf,inf,inf,inf,inf,inf],[inf,inf,inf,inf,inf,inf]]
print(Floyd_Warshall(G))
G=[[(1,2),(3,2)],[(0,2),(2,3),(3,5),(4,1),(5,7)],[(1,3),(3,1)],
[(0,2),(1,5),(2,1)],[(1,1),(5,4)],[(3,7),(4,4)]]
print(not_directed(G))
G=[[(1,2),(2,7),(3,1)],[(0,2),(2,2),(3,3)],
[(0,7),(1,2),(3,3)],[(0,1),(1,3),(2,3)]]
print(not_directed(G))
G=[[(1,3)],[(0,3),(2,7)],[(1,7),(3,5)],[(2,5),(4,11),(5,17)],[(3,11)],[(3,17)]]
print(not_directed(G))
