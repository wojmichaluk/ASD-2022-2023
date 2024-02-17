#Wojciech Michaluk
#Algorytm najpierw przepisuje graf na postać
#listową. Następnie, aby znaleźć minimalny
#czas podróży z zamku s do t, wykorzystuje
#lekko zmodyfikowany algorytm Dijkstry -
#znajduje minimalny czas dotarcia do danego
#zamku i mając już "za sobą" - od ostatniego
#noclegu, przy czym z zamku s rycerz wyjeżdża
#wyspany - daną liczbę godzin (od 0 do 16
#włącznie). Korzystając z warunków zadania
#(krawędzi jest O(n)), szacuję złożoność
#czasową algorytmu na O(n^2), natomiast
#pamięciową na O(n).

from egz3atesty import runtests
from queue import PriorityQueue

#O(n^2)
def goodknight( G, s, t ):
    n=len(G)
    Gr=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]!=-1:
                Gr[i].append((G[i][j],j))
    d=[[float('inf') for _ in range(17)] for _ in range(n)]
    d[s][0]=0
    Q=PriorityQueue()
    Q.put((0,0,s))
    while not Q.empty():
        w,h,u=Q.get()
        if w==d[u][h]:
            for c,v in Gr[u]:
                res=relax(d,v,c,u,h)
                if res==1: Q.put((d[v][h+c],h+c,v))
                elif res==2: Q.put((d[v][c],c,v))
    return min(d[t])
    
def relax(d,v,c,u,h):
    if h+c<=16:
        if d[v][h+c]>d[u][h]+c:
            d[v][h+c]=d[u][h]+c
            return 1
    else:
        if d[v][c]>d[u][h]+c+8:
            d[v][c]=d[u][h]+c+8
            return 2
    return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )

#testy kontrolne, do sprawdzenia poprawności
"""
G=[[-1, 8, -1, -1, -1, 8, -1, -1, -1],
[ 8, -1, 1, -1, -1, -1, -1, -1, -1],
[-1, 1, -1, 8, -1, -1, -1, -1, -1],
[-1, -1, 8, -1, 4, -1, -1, -1, -1],
[-1, -1, -1, 4, -1, -1, -1, -1, 5],
[ 8, -1, -1, -1, -1, -1, 8, -1, -1],
[-1, -1, -1, -1, -1, 8, -1, 8, -1],
[-1, -1, -1, -1, -1, -1, 8, -1, 8],
[-1, -1, -1, -1, 5, -1, -1, 8, -1]]
print(goodknight(G,0,8)) #40

G=[[-1, 8, -1, -1, -1, 8, -1, -1],
[ 8, -1, 1, -1, -1, -1, -1, -1],
[-1, 1, -1, 8, -1, -1, -1, -1],
[-1, -1, 8, -1, 1, -1, -1, -1],
[-1, -1, -1, 1, -1, -1, 5, 8],
[ 8, -1, -1, -1, -1, -1, 8, -1],
[-1, -1, -1, -1, 5, 8, -1, -1],
[-1, -1, -1, -1, 8, -1, -1, -1]]
print(goodknight(G,0,7)) #37
"""
