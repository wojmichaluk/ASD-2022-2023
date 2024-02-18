#liczba spójnych składowych (DFS),
#mamy listę sąsiedztwa

#zadanie 1b
def connected(G):
    vis=[0]*len(G)
    def DFS(G,v):
        nonlocal vis
        vis[v]=1
        for u in G[v]:
            if vis[u]: continue
            DFS(G,u)
    cnt=0
    for i in range(len(G)):
        if not vis[i]:
            cnt+=1
            DFS(G,i)
    return cnt

#testy
G=[[3,4],[3,5],[3,5],[0,1,2],[0],[1,2]]
print(connected(G))
G=[[2,3,4],[],[0,4],[0,4],[0,2,3]]
print(connected(G))
G=[[1,2],[0,2],[0,1],[4,5],[3,5],[3,4],[7],[6]]
print(connected(G))
G=[[1],[0,2],[1,3],[2,4,7],[3,5],[4],[7],[3,6]]
print(connected(G))
