#Dana jest szachownica n x n, każde pole
#ma koszt 1,2,3,4 lub 5. Szukamy minimalnego
#kosztu przejścia z lewego górnego rogu do
#prawego dolnego rogu. Pomysł: BFS, wrzucamy
#do kolejki parę (wierzchołek, koszt). Jeżeli
#przy pobieraniu koszt==1 to normalny BFS,
#w przeciwnym razie z powrotem wrzucamy do
#kolejki wierzchołek z kosztem zmniejszonym
#o 1 i uaktualniamy "odległość" wierzchołka +=1.

from queue import Queue

#zadanie 6
def cheapest(G):
    n=len(G)
    vis=[[0 for _ in range(n)] for _ in range(n)]
    d=[[-1 for _ in range(n)] for _ in range(n)]
    q=Queue()
    d[0][0]=0
    vis[0][0]=1
    q.put((0,0,G[0][0]))
    while not q.empty():
        v=q.get()
        if v[0]==v[1]==n-1:
            return d[n-1][n-1]+v[2]
        d[v[0]][v[1]]+=1
        if v[2]>1: q.put((v[0],v[1],v[2]-1))
        else:
            if v[0]>0:
                if not vis[v[0]-1][v[1]]: 
                    q.put((v[0]-1,v[1],G[v[0]-1][v[1]]))
                    d[v[0]-1][v[1]]=d[v[0]][v[1]]
                    vis[v[0]-1][v[1]]=1
            if v[0]<n-1:
                if not vis[v[0]+1][v[1]]:
                    q.put((v[0]+1,v[1],G[v[0]+1][v[1]]))
                    d[v[0]+1][v[1]]=d[v[0]][v[1]]
                    vis[v[0]+1][v[1]]=1
            if v[1]>0:
                if not vis[v[0]][v[1]-1]:
                    q.put((v[0],v[1]-1,G[v[0]][v[1]-1]))
                    d[v[0]][v[1]-1]=d[v[0]][v[1]]
                    vis[v[0]][v[1]-1]=1
            if v[1]<n-1:
                if not vis[v[0]][v[1]+1]:
                    q.put((v[0],v[1]+1,G[v[0]][v[1]+1]))
                    d[v[0]][v[1]+1]=d[v[0]][v[1]]
                    vis[v[0]][v[1]+1]=1

#testy
G=[[2,3,1,5],[4,1,3,2],[2,3,2,2],[5,1,5,2]]
print(cheapest(G))
G=[[3,4,1,4,3,2],[2,5,3,1,2,4],[5,2,5,3,1,4],
[2,3,1,5,4,3],[1,1,3,1,2,1],[4,5,3,4,5,2]]
print(cheapest(G))
