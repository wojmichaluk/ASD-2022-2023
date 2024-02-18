#Stacja benzynowa - chcemy dojechać
#z miasta s do miasta e. Znamy odległości
#między miastami w km, w każdym mieście jest
#dana cena paliwa. Spalamy 1l/1km, zaczynamy
#z pustym bakiem. Szukamy najtańszego przejazdu.
#Ułatwienie: tankujemy dokładnie tyle, ile 
#potrzeba na przejechanie do sąsiedniego miasta
#(nie robimy zapasów). D - pojemność baku.

from math import inf
from queue import PriorityQueue

#zadanie 9
#wersja uproszczona - ze ścieżką
def relax(par,d,v,c,u):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

def cheapest(G,s,e,D):
    n=len(G)
    d=[inf for _ in range(n)]
    par=[None for _ in range(n)]
    d[s]=0
    q=PriorityQueue()
    q.put((0,s)) 
    while not q.empty():
        w,u = q.get()
        if w==d[u]:
            for v,c in G[u][0]:
                if c<=D:
                    if relax(par,d,v,c*G[u][1],u):
                        q.put((d[v],v))
    path=[]
    t=e
    while t!=None:
        path.append(t)
        t=par[t]
    path.reverse()
    return d[e],path

#wersja realna
def cheapest2(G,start,end,D):
    n=len(G)
    Graph=[[inf for _ in range(D+1)] for _ in range(n)]
    d=[inf for _ in range(n)]
    q=PriorityQueue()
    q.put((0,0,start))
    while not q.empty():
        c,f,v=q.get()
        if d[v]>c:
            d[v]=c
        for i in range(D+1-f):
            if c+i*G[v][1]<Graph[v][i+f]:
                Graph[v][i+f]=c+i*G[v][1]
                for u,e in G[v][0]:
                    if i+f>=e:
                        q.put((c+i*G[v][1],i+f-e,u))
    return d[end]

#testy
G=[[[(1,42),(4,35)],5.70],[[(0,42),(2,25),(4,15)],6.20],
[[(1,25),(3,31),(5,65)],6.05],[[(2,31),(5,42)],5.10],
[[(0,35),(1,15),(5,52)],5.30],[[(2,65),(3,42),(4,52)],4.90]]
print(cheapest(G,0,3,50))
print(cheapest2(G,0,3,50))
G=[[[(1,5),(2,7)],8],[[(0,5),(2,3),(3,5)],5],
[[(0,7),(1,3),(3,4)],3],[[(1,5),(2,4),(4,6)],2],[[(3,6)],1]]
print(cheapest(G,0,4,6))
print(cheapest2(G,0,4,6))
G=[[[(1,5),(2,7)],2],[[(0,5),(2,3),(3,5)],7],
[[(0,7),(1,3),(3,4)],9],[[(1,5),(2,4),(4,6)],4],[[(3,6)],7]]
print(cheapest(G,0,4,6))
print(cheapest2(G,0,4,6))
