#Wojciech Michaluk
#Algorytm w celu znalezienia optymalnej
#kolejności instalowania plików systemu
#traktuje tablicę zależności jako skierowany
#graf (acykliczny) i sortuje go topologicznie.
#Dzięki założeniom zadania można wykorzystać
#to sortowanie. Następnie przechodzi po kolei
#w tablicy plików, które mają być instalowane
#po kolei i zlicza każdą potrzebną zmianę
#dyskietki. Szacuję złożoność czasową na O(n),
#a pamięciową na O(k), gdzie k - liczba plików.

from kolutesty import runtests

def swaps( disk, depends ):
    n=len(depends)
    G=[[depends[i][j] for j in range(len(depends[i]))] for i in range(n)]
    flag=False
    min_index=-1
    for i in range(n):
        if not G[i]:
            if not flag:
                flag=True
                min_index=i
            else:
                G[i]=[min_index]
    order=topo_sort(G)
    m=len(order)
    changes=0
    last=disk[order[0]]
    for i in range(1,m):     
        if disk[order[i]]!=last:
            changes+=1
        last=disk[order[i]]
    return changes

def DFS(G,u,visited,done):
    visited[u]=True
    for v in G[u]:
        if not visited[v]:
            DFS(G,v,visited,done)
    done.append(u)

def topo_sort(G):
    n=len(G)
    visited=[False for _ in range(n)]
    done=[]
    DFS(G,0,visited,done)
    return done
    
# zmien all_tests na True zeby uruchomic wszystkie testy
#nie działa, błędy w implementacji
runtests( swaps, all_tests = True )

