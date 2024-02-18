#Graf reprezentuje sieć drogową, wierzchołki
#są miastami, krawędzie to drogi (długości w km).
#Alice i Bob się zmieniają po każdym mieście. 
#Wyznaczamy, kto zaczyna w mieście start i drogę
#tak, Żeby Alice jechała jak najmniej. Pomysł:
#1) Wariancja Dijkstry, wydłużamy długość tylko wtedy,
#gdy jedzie Alice. 2) Modyfikujemy graf - podwajamy
#wierzchołki, jeżeli jedzie Alice to zostawiamy
#oryginalną wagę, dla Boba waga krawędzi to 0.
#Na przemian są krawędzie dla Alice i Boba.

from math import inf
from queue import PriorityQueue
from queue import Queue

#zadanie 4
def Dijkstra_mod(G,start,who,end):
    n=len(G)
    d=[inf for _ in range(n)]
    d[start]=0
    Q=PriorityQueue()
    Q.put((0,start,who,[]))
    while not Q.empty():
        w,u,z,p=Q.get()
        if u==end:
            return d[end],p+[u]
        for v,c in G[u]:
            if z=='B':
                if d[v]>w:
                    d[v]=w
                Q.put((d[v],v,'A',p+[u]))
            elif d[v]>w+c:
                d[v]=w+c
                Q.put((d[v],v,'B',p+[u]))
            else:
                if not u in p: Q.put((d[u]+c,v,'B',p+[u]))

def relax(par,d,v,c,u):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

def shortest(G,start,end):
    a1=Dijkstra_mod(G,start,'A',end)
    a2=Dijkstra_mod(G,start,'B',end)
    if a1[0]<a2[0]:
        return a1
    return a2

#ma sens tylko, gdy graf dwudzielny
def shortest2(G,start,end):
    a=bipartite(G,start)
    if not a:
        return "not bipartite"
    n=len(G)
    Gr=[[G[i][j] for j in range(len(G[i]))] for i in range(n)]
    for i in range(n):
        if a[1][i]==0:
            for j in range(len(G[i])):
                G[i][j]=(G[i][j][0],0)
        else:
            for j in range(len(Gr[i])):
                Gr[i][j]=(Gr[i][j][0],0)
    a1=Dijkstra(G,start)
    a2=Dijkstra(Gr,start)
    path=[]
    k=end
    if a1[1][end]<a2[1][end]:
        while k!=None:
            path.append(k)
            k=a1[0][k]
        l=a1[1][end]
    else:
        while k!=None:
            path.append(k)
            k=a2[0][k]
        l=a2[1][end]
    path.reverse()
    return l,path

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

#zmodyfikowana funkcja z cw 6 zadanie 1a
def bipartite(G,start_v):
    colors=[-1]*len(G)
    q=Queue()
    q.put(start_v)
    colors[start_v]=0
    while not q.empty():
        v=q.get()
        for u in G[v]:
            if colors[u[0]]==-1:
                colors[u[0]]=(colors[v]+1)%2
                q.put(u[0])
            else:
                if colors[u[0]]==colors[v]: return False
    return True,colors

#testy
G=[[(2,50),(3,60)],[(2,70),(3,30)],[(0,50),(1,70)],[(0,60),(1,30)]]
print(shortest(G,0,1))
print(shortest2(G,0,1))
G=[[(2,50),(3,60)],[(2,70),(3,30)],[(0,50),(1,70),(3,25)],[(0,60),(1,30),(2,25)]]
print(shortest(G,0,1))
print(shortest2(G,0,1))
G=[[(1,100),(2,90),(3,40)],[(0,100),(5,20)],[(0,40),(4,50)],[(0,90),(4,15),(5,25)],
[(2,50),(3,15),(6,70)],[(1,20),(3,25),(6,35)],[(4,70),(5,35)]]
print(shortest(G,0,6))
print(shortest2(G,0,6))
