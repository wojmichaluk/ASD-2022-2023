#Wojciech Michaluk
#Algorytm najpierw "rozdwaja" każdy
#wierzchołek, co odpowiada sytuacjom:
#1) wjechano do tego zamku i rycerz go nie
#napada, 2) rycerz napada na ten zamek.
#Następnie przechodzi po tym grafie, dla
#każdego wierzchołka wyznacza minimalny
#koszt wejścia do niego (algorytm Dijkstry),
#uwzględniając przy tym warunki zadania.
#Szacuję złożoność czasową algorytmu na
#O(V^2logV), a pamięciową na O(V).

from egz1Atesty import runtests
from queue import PriorityQueue

def gold(G,V,s,t,r):
    n=len(G)
    Gr=[[] for _ in range(2*n)]
    for i in range(n):
        for j in range(len(G[i])):
            Gr[i].append(G[i][j])
            Gr[i+n].append((G[i][j][0]+n,2*G[i][j][1]+r))
            Gr[i].append((i+n,0))
    #algorytm Dijkstry
    d=[float('inf') for _ in range(2*n)]
    d[s]=0
    q=PriorityQueue()
    q.put((0,s))
    while not q.empty():
        w,u=q.get()
        if d[u]==w:
            for v,c in Gr[u]:
                if v>=n and u<n:
                    if relax(u,d,v,-V[u]):
                        q.put((d[v],v))
                else:
                    if relax(u,d,v,c):
                        q.put((d[v],v))
    return min(d[t],d[t+n])

def relax(u,d,v,c):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        return True
    return False

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
