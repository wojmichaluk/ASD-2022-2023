#Wojciech Michaluk
#Algorytm wykorzystuje DFS do przejścia po grafie
#(miastach), przy czym jeżeli wszedł bramą północną
#to wychodzi południową i vice-versa. Dla ustalenia
#uwagi zaczyna z miasta 0, badając obie możliwości
#wyjścia bramami (bo jeżeli taka droga istnieje, to
#nie ważne skąd zaczniemy) - po znalezieniu drogi 
#sprawdza, czy spełnia ona warunki zadania. Szacuję 
#złożoność czasową algorytmu na O(V^2+VE), a
#pamięciową na O(V) dodatkowej pamięci, gdzie V - 
#liczba wierzchołków a E - liczba krawędzi.

from zad7testy import runtests

#wersja 1
def droga( G ):
    path=DFS(G,1)
    if correct_path(G,1,path):
        return path
    path=DFS(G,0)
    if correct_path(G,0,path):
        return path

def DFS(G,d):
    n=len(G)
    visited=[False for _ in range(n)]
    vertices=[]
    DFSVisit(G,0,d,visited,vertices)
    vertices.reverse()
    return vertices

def DFSVisit(G,v,d,vis,ver,cnt=0):
    vis[v]=True
    if cnt<len(G):
        for u in G[v][1-d]:
            if not vis[u]:
                if v in G[u][0]:
                    DFSVisit(G,u,0,vis,ver,cnt+1)
                else:
                    DFSVisit(G,u,1,vis,ver,cnt+1)
        ver.append(v)

def correct_path(G,dir,vertices):
    n=len(G)
    d=dir
    for i in range(n-1):
        if not vertices[i+1] in G[vertices[i]][1-d]:
            return False
        if vertices[i] in G[vertices[i+1]][0]: d=0
        else: d=1
    if not vertices[0] in G[vertices[n-1]][1-d] or not vertices[n-1] in G[vertices[0]][dir]:
        return False
    return True

#wersja 2
"""def droga( G ):
    path=DFS(G,1)
    if path: return path
    return DFS(G,0)

def DFS(G,d):
    n=len(G)
    visited=[False for _ in range(n)]
    vertices=[0]
    return DFSVisit(G,0,d,visited,vertices)

def DFSVisit(G,v,d,vis,ver):
    if len(ver)<len(G):
        curr_vis=vis.copy()
        curr_vis[v]=True
        for u in G[v][1-d]:
            if not curr_vis[u]:
                if v in G[u][0]:
                    a=DFSVisit(G,u,0,curr_vis,ver+[u])
                else:
                    a=DFSVisit(G,u,1,curr_vis,ver+[u])
                if a: return a
    elif correct_path(G,0,ver) or correct_path(G,1,ver):
        return ver

def correct_path(G,dir,vertices):
    n=len(G)
    d=dir
    for i in range(n-1):
        if not vertices[i+1] in G[vertices[i]][1-d]:
            return False
        if vertices[i] in G[vertices[i+1]][0]: d=0
        else: d=1
    if not vertices[0] in G[vertices[n-1]][1-d] or not vertices[n-1] in G[vertices[0]][dir]:
        return False
    return True"""

# zmien all_tests na True zeby uruchomic wszystkie testy
#kod niestety nie jest poprawny
runtests( droga, all_tests = True )
