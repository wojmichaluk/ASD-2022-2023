#cykl Eulera
def EulerCycle(G,start_v):
    def DFSVisit(G,u):
        nonlocal cycle
        for i in range (len(G[u])):
            if G[u][i]:
                G[u][i]=0
                G[i][u]=0
                DFSVisit(G,i)
        cycle.append(u)
    n=len(G)
    M=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            M[i][j]=1
    cycle=[]
    DFSVisit(M,start_v)
    return cycle[::-1]

#silnie spójne składowe
def strongly_coherent(G):
    def DFSVisit(G,u,coherent=-1):
        nonlocal time
        nonlocal times
        nonlocal visited
        if coherent!=-1: coherent.append(u)
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G,v,coherent)
        time+=1
        times[u]=time
    n=len(G)
    visited=[False for _ in range(n)]
    times=[None for _ in range(n)]
    time=0
    for i in range(n):
        if not visited[i]: DFSVisit(G,i)
    T=[-1 for _ in range(n)]
    for i in range(n):
        T[n-times[i]]=i
    visited=[False for _ in range(n)]
    Gr=[[] for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            Gr[G[i][j]].append(i)
    coherent=[]
    k=0
    for i in range(n):
        if not visited[T[i]]:
            coherent.append([])
            DFSVisit(Gr,T[i],coherent[k])
            k+=1
    return coherent

#znajdowanie mostów
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
G=[[1,3],[0,2],[1,3],[0,2]]
print(EulerCycle(G,0))
G=[[1,2],[0,2,3,4,5,6],[0,1,3,4,5,6],[1,2,4,5],[1,2,3,5],[1,2,3,4],[1,2]]
print(EulerCycle(G,0))
G=[[1],[2],[0,3],[4],[5],[3]]
print(strongly_coherent(G))
G=[[1],[2],[0,3,8],[4,6],[5],[3],[5],[8],[9],[5,10],[3,7]]
print(strongly_coherent(G))
G=[[1,6],[0,2],[1,3,6],[2,4,5],[3,5],[3,4],[0,2,7],[6]]
print(bridges(G))
G=[[1,5,12],[0,2],[1,3,6],[2,4],[3,5],[0,4],[2,7,8],[6,8],[6,7,9],
[8,10,11],[9,11],[9,10],[0,13,15],[12,14],[13,15],[12,14]]
print(bridges(G))

G=[[1],[0,2],[1,3,4],[2,5],[2,5],[3,4]]
print(strongly_coherent(G))
