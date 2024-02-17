#Wojciech Michaluk
#Algorytm najpierw buduje reprezentację grafu
#w postaci listy krawędzi. Następnie je sortuje
#oraz przegląda każde "okno" n-1 bezpośrednio
#kolejnych krawędzi (n to liczba wierzchołków),
#jeżeli dla badanego okna graf jest spójny, to
#oznacza, że znaleźliśmy drzewo, które jest piękne
#(bo krawędzie są kolejnymi); wynika to z własności
#drzewa (grafu). Szacuję złożoność czasową algorytmu
#na O(VE), a złożoność pamięciową na O(E).

from kol2testy import runtests

def beautree(G):
    F=[]
    n=len(G)
    for i in range(n):
        for j,w in G[i]:
            F.append((w,i,j))
    F.sort()
    m=len(F)
    E=[]
    for i in range(0,m,2):
        E.append(F[i])
    found=DFS(E,n)
    if found==None:
        return None
    suma=E[found][0]
    for i in range(found+1,found+n-1):
        suma+=E[i][0]
    return suma

def DFS(E,n):
    G=[[] for _ in range(n)]
    for i in range(n-1):
        w,u,v=E[i]
        G[u].append(v)
        G[v].append(u)
    b=0
    m=len(E)
    while b<=m-n:
        visited=[False for _ in range(n)]
        DFSVisit(G,0,visited)
        if coherent(visited): return b
        update(E,G,b)
        b+=1
    return None
    	
def DFSVisit(G,v,visited):
    visited[v]=True
    for u in G[v]:
        if not visited[u]:
            DFSVisit(G,u,visited)
            
def coherent(visited): 
    n=len(visited)      
    for i in range(n):
        if not visited[i]: return False
    return True
    
def update(E,G,b):
    w,u,v=E[b]
    for i in range(len(G[u])):
        if G[u][i]==v: 
            G[u].pop(i)
            break
    for i in range(len(G[v])):
        if G[v][i]==u: 
            G[v].pop(i)
            break
    n=len(G)
    w,u,v=E[b+n-1]
    G[u].append(v)
    G[v].append(u)

# zmien all_tests na True zeby uruchomic wszystkie testy
#prawdopodobnie optymalizacja możliwa, ale czas w porządku
runtests( beautree, all_tests = True )

