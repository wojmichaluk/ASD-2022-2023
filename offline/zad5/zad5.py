#Wojciech Michaluk
#Algorytm najpierw "przepisuje" listę opisującą planety
#na graf reprezentowany przez listę sąsiedztwa oraz
#planety przy osobliwości łączy krawędziami o czasie
#podróży 0 w cyklu. Następnie przechodzi po tym grafie
#podobnie jak w algorytmie BFS i zapisuje dla każdego
#wierzchołka minimalny koszt podróży (jeżeli koszt przejścia
#do wierzchołka po danej krawędzi jest mniej opłacalny
#niż dotychczasowy koszt - nie przechodzimy.  Jeżeli da się
#dojść do planety b, zwracamy koszt dojścia do niej, jeżeli nie
#to None. Złożoność algorytmu szacuję na O(ElogV), gdzie E to
#długość listy E (liczba krawędzi), V - liczba planet.

from zad5testy import runtests
from collections import deque

def spacetravel( n, E, S, a, b ):
    G=[[] for _ in range(n)]
    for i in range(len(E)):
        c=E[i]
        G[c[0]].append((c[1],c[2]))
        G[c[1]].append((c[0],c[2]))
    d=[float('inf') for _ in range(n)] 
    for i in range(-1,len(S)-1):
        G[S[i]].append((S[i+1],0))
        G[S[i+1]].append((S[i],0))
    q=deque()
    q.append(a)
    d[a]=0
    while q:
        v=q.popleft()
        for u in G[v]:
            if d[u[0]]>d[v]+u[1]:
                d[u[0]]=d[v]+u[1]
                q.append(u[0])
    if d[b]!=float('inf'): return d[b]
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
