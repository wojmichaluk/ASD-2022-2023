#Wojciech Michaluk
#Algorytm najpierw przepisuje listę miast na
#graf w postaci listy krawędzi, w którym
#wierzchołki to miasta, a wagi krawędzi to
#odległości między miastami (każdą parę miast
#łączymy). Następnie sortuje krawędzie i szuka
#MST algorytmem Kruskala, bazując na strukturze
#find / union. Aby zminimalizować różnicę,
#usuwamy krawędzie z początku, dopóki istnieje
#drzewo rozpinające. Szacuję złożoność algorytmu
#na O(V^4log*V^2), gdzie V - liczba wierzchołków,
#a log* - logarytm iterowany.

from zad8testy import runtests

def highway( A ):
    n=len(A)
    E=[]
    for i in range(n-1):
        for j in range(i+1,n):
            w=edge_weight(A[i],A[j])
            E.append((w,i,j))
    E.sort()
    min_time=kruskal(E,0,n)
    for i in range(1,len(E)-n+2):
        min_time=min(min_time,kruskal(E,i,n))
    return min_time

class Node:
    def __init__(self,value):
        self.parent=self
        self.rank=0
        self.value=value

def findset(x):
    if x.parent!=x:
        x.parent=findset(x.parent)
    return x.parent

def union(x,y):
    x=findset(x)
    y=findset(y)
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1

def edge_weight(u,v):
    w=((u[0]-v[0])**2+(u[1]-v[1])**2)**0.5
    if int(w)<w: return int(w+1)
    return int(w)

def kruskal(E,i,n):
    A=[]
    V=[Node(j) for j in range(n)]
    for j in range(i,len(E)):
        w,u,v=E[j]
        if findset(V[u])!=findset(V[v]):
            A.append(w)
            union(V[u],V[v])
    if len(A)<n-1:
        return float('inf')
    return A[-1]-A[0]

# zmien all_tests na True zeby uruchomic wszystkie testy
#nienajlepsza złożoność
runtests( highway, all_tests = True )
