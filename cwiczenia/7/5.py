#Szukanie mostu w grafie.

#zadanie 5
def bridges(G):
    def DFSVisit(G,u):
        nonlocal time
        nonlocal times
        nonlocal visited
        nonlocal parent
        nonlocal low
        time+=1
        times[u]=time
        visited[u]=True
        anc=[]
        desc=[]
        for v in G[u]:
            if not visited[v]:
                desc.append(v)
                parent[v]=u
                DFSVisit(G,v)
            elif v!=parent[u]: anc.append(v)
        min_u=len(G)+1
        for i in range(len(anc)):
            if times[anc[i]]<min_u: min_u=times[anc[i]]
        min_w=len(G)+1
        for i in range(len(desc)):
            if low[desc[i]]<min_w: min_w=low[desc[i]]
        low[u]=min(times[u],min_u,min_w)
    n=len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    times=[None for _ in range(n)]
    low=[None for _ in range(n)]
    bridge=[]
    time=0
    for i in range(n):
        if not visited[i]: DFSVisit(G,i)
    for i in range(n):
        if parent[i]!=None and times[i]==low[i]:
            bridge.append((parent[i],i))
    return bridge

#testy
G=[[1,6],[0,2],[1,3,6],[2,4,5],[3,5],[3,4],[0,2,7],[6]]
print(bridges(G))
G=[[1,3],[0,2],[1,3],[0,2]]
print(bridges(G))
G=[[1,5,12],[0,2],[1,3,6],[2,4],[3,5],[0,4],[2,7,8],[6,8],[6,7,9],
[8,10,11],[9,11],[9,10],[0,13,15],[12,14],[13,15],[12,14]]
print(bridges(G))
G=[[1,8],[0,2],[1,3],[2,4],[3,5,7],[4,6],[5,7],[4,6,8],[7,0]]
print(bridges(G))
