#Wojciech Michaluk
#Algorytm dla danego miasta, w którym odkryto
#nowe źródło, sprawdza kombinację każdych dwóch
#innych miast, w których można umieścić oczyszczalnie
#i wylicza dla nich maksymalny przepływ, korzystając z
#algorytmu Forda-Fulkersona, następnie z wyliczonych
#wartości bierze maksimum. Szacuję złożoność czasową
#algorytmu na O(V^3E^2), a pamięciową na O(V^2),
#gdzie V oznacza liczbę miast, E - liczbę rurociągów.

from zad9testy import runtests
from queue import Queue

def maxflow( G,s ):
    cities=0
    n=len(G)
    for i in range(n):
        cities=max(cities,G[i][1])
    cities+=1
    Gr=[[0 for _ in range(cities+1)] for _ in range(cities+1)]
    for u,v,f in G:
        Gr[u][v]=f
    max_flow=0
    for i in range(cities):
        if i==s: continue
        for j in range(i+1,cities):
            if j==s: continue
            Gr[i][cities]=Gr[j][cities]=float('inf')
            max_flow=max(max_flow,FF(Gr,s,cities))
            Gr[i][cities]=Gr[j][cities]=0
    return max_flow

def FF(G,s,t): #metoda Forda-Fulkersona
    flow=0
    n=len(G)
    Gr=[[G[i][j] for j in range(n)] for i in range(n)]
    path=BFS(Gr,s,t)
    while path:
        w=cap(Gr,path)
        flow+=w
        update(Gr,path,w)
        path=BFS(Gr,s,t)
    return flow

def cap(G,path): #pojemnosc sciezki
    minf=G[path[0]][path[1]]
    for i in range(1,len(path)-1):
        minf=min(minf,G[path[i]][path[i+1]])
    return minf

def update(G,path,w): #zmiana wag krawedzi
    for i in range(len(path)-1):
        G[path[i]][path[i+1]]-=w
        G[path[i+1]][path[i]]+=w

def BFS(G,s,t): #znajdowanie sciezki
    n=len(G)
    par=[None for _ in range(n)]
    visited=[False for _ in range(n)]
    q=Queue()
    q.put(s)
    visited[s]=True
    while not q.empty():
        v=q.get()
        if v==t: break
        for i in range(n):
            if G[v][i]>0 and not visited[i]:
                par[i]=v
                visited[i]=True
                q.put(i)
    k=t
    path=[]
    while k!=None:
        path.append(k)
        k=par[k]
    if len(path)<2: return None
    path.reverse()
    return path

# zmien all_tests na True zeby uruchomic wszystkie testy
#złożoność nienajlepsza
runtests( maxflow, all_tests = True )
