#Wojciech Michaluk
#Algorytm używa przejścia przez graf BFS, który
#opiera się na zaimplementowanej w postaci listy
#odsyłaczowej kolejce. Najpierw znajduję najkrótszą
#ścieżkę (długość i krawędzie ją tworzące), potem
#badam długość (nowej) ścieżki po usunięciu w grafie
#po kolei jednej z krawędzi z pierwotnej ścieżki. Jeżeli
#nowa długość jest większa niż pierwotna, dana
#krawędź jest szukaną krawędzią. Szacuję złożoność
#obliczeniową algorytmu na O(||V||^2), gdzie ||V||
#oznacza liczbę wierzchołków.

from zad4testy import runtests

class queue:
    def __init__(self):
        self.size=0
        self.first=None
        self.last=None

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def put(Q,val):
    if not Q.size:
        Q.first=Q.last=Node(val)
        Q.size=1
        return
    Q.last.next=Node(val)
    Q.last=Q.last.next
    Q.size+=1

def get(Q):
    val=Q.first.val
    Q.first=Q.first.next
    Q.size-=1
    return val
    
def longer( G, s, t ):
    q=queue()
    visited=[False]*len(G)
    d=[-1]*len(G)
    parent=[None]*len(G)
    put(q,(s,0))
    visited[s]=True
    while q.size:
        v=get(q)
        d[v[0]]=v[1]
        if v[0]==t: break
        for u in G[v[0]]:
            if visited[u]: continue
            visited[u]=True
            parent[u]=v[0]
            put(q,(u,v[1]+1))
    if  not visited[t]: return None
    path=[]
    length=d[t]
    k=t
    while k!=s:
        path.append((parent[k],k))
        k=parent[k]
    for edge in path:
        if BFS(G,s,t,edge[0],edge[1])>length: return edge
    return None

def BFS(G,s,t,f1,f2):
    q=queue()
    visited=[False]*len(G)
    d=[-1]*len(G)
    put(q,(s,0))
    visited[s]=True
    while q.size:
        v=get(q)
        d[v[0]]=v[1]
        if v[0]==t: break
        for u in G[v[0]]:
            if (u==f1 and v[0]==f2) or (u==f2 and v[0]==f1): continue
            if visited[u]: continue
            visited[u]=True
            put(q,(u,v[1]+1))
    if not visited[t]: return float('inf')
    return d[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
