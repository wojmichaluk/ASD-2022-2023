#Operator telefonii komórkowej usuwa sieć z Polski,
#zaproponuj kolejność usuwania stacji, aby graf
#pozostał spójny. Pomysł: DFS - zaczynamy z dowolnego
#wierzchołka, dodajemy do listy do usunięcia wierzchołek,
#kiedy zostanie on przetworzony (dodajemy na koniec).
#BFS - do listy wskazującej kolejność usuwania dodajemy
#wierzchołki w odwrotnej kolejności niż nr fali, w której
#zostały pokryte.

from queue import Queue

#zadanie 2
def DFS(G):
    def DFSVisit(G,u):
        nonlocal visited
        nonlocal que
        visited[u]=True
        for v in G[u]:
            if not visited[v]: DFSVisit(G,v)
        que.append(u)
    n=len(G)
    visited=[False for _ in range(n)]
    que=[]
    for i in range(n):
        if not visited[i]: DFSVisit(G,i)
    return que

def BFS(G,s):
    q=Queue()
    n=len(G)
    visited=[False for _ in range(n)]
    d=[-1 for _ in range(n)]
    d[s]=0
    visited[s]=True
    q.put(s)
    while not q.empty():
        v=q.get()
        for u in G[v]:
            if not visited[u]:
                d[u]=d[v]+1
                visited[u]=True
                q.put(u)
    que=[(d[i],i) for i in range(n)]
    que.sort()
    que=[que[i][1] for i in range(n)]
    return que[::-1]

#testy
G=[[1],[0,2],[1,3],[2,4,7],[3,5],[4],[7],[3,6]]
print(*DFS(G))
print(*BFS(G,0))
G=[[3,4],[3,5],[3,5],[0,1,2],[0],[1,2]]
print(*DFS(G))
print(*BFS(G,0))
