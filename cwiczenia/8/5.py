#Mamy kantor, a w nim kursy wymiany walut
#(jako graf skierowany). Szukamy, czy możemy
#zyskać. Pomysł: bierzemy ln, uruchamiamy
#Bellmana - Forda i sprawdzamy, czy istnieje
#cykl o ujemnej wadze.

from math import inf
from math import log

#zadanie 5
def Bellman_Ford(G): #modyfikacja z zadania 6
    n=len(G)
    visited=[False for _ in range(n)]
    d=[inf]*n
    for i in range(n):
        for j in range(n):
            G[i][j]=log(G[i][j])
    par=[None]*n
    for h in range(n):
        if not visited[h]:
            d[h]=0
            for i in range(n):
                B=False
                for j in range(n):
                    for k in range(n):
                        B|=relax(par,d,j,k,G)
                        if d[k]!=inf: visited[k]=True
    #return d,par,B
    return B

def relax(par,d,i,j,G):
    if d[j]>d[i]+G[i][j]:
        d[j]=d[i]+G[i][j]
        par[j]=i
        return True
    return False

#testy
G=[[inf,0.9,inf,1.3,inf],[inf,inf,0.72,inf,12.15],[1.5,inf,inf,1.12,inf],
[inf,1.7,inf,inf,19.5],[0.12,0.09,inf,inf,inf]]
print(Bellman_Ford(G))
G=[[inf,1.05,inf,inf,inf,inf],[inf,inf,1.05,inf,inf,inf],[1.05,inf,inf,inf,inf,inf],
[inf,inf,inf,inf,0.95,inf],[inf,inf,inf,inf,inf,0.95],[inf,inf,inf,0.95,inf,inf]]
print(Bellman_Ford(G))
G=[[inf,1.07,1.11,1.01],[1.03,inf,0.99,1.04],[1.12,1.21,inf,1.15],[1.03,0.98,1.1,inf]]
print(Bellman_Ford(G))
