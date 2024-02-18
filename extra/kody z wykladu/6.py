from queue import Queue

#breadth-first search
def BFS(G,s):
    q=Queue()
    n=len(G)
    visited=[False for _ in range(n)]
    d=[-1 for _ in range(n)]
    parent=[None for _ in range(n)]
    d[s]=0
    visited[s]=True
    q.put(s)
    while not q.empty():
        v=q.get()
        for u in G[v]:
            if not visited[u]:
                d[u]=d[v]+1
                parent[u]=v
                visited[u]=True
                q.put(u)
    return d,parent,visited

#depth-first-search
def DFS(G):
    def DFSVisit(G,u):
        nonlocal time
        nonlocal times
        nonlocal visited
        nonlocal parent
        time+=1
        times[u]=time
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                parent[v]=u
                DFSVisit(G,v)
        time+=1
        times[u]=(times[u],time)
    n=len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    times=[None for _ in range(n)]
    time=0
    for i in range(n):
        if not visited[i]: DFSVisit(G,i)
    return parent,times

#sortowanie topologiczne - wykorzystanie DFS
def topological_sort(G):
    def DFSVisit(G,u):
        nonlocal to_do_list
        nonlocal visited
        visited[u]=True
        for v in G[u]:
            if not visited[v]: DFSVisit(G,v)
        to_do_list.append(u)
    n=len(G)
    visited=[False for _ in range(n)]
    to_do_list=[]
    for i in range(n):
        if not visited[i]: DFSVisit(G,i)
    return to_do_list[::-1]

#testy
G=[[1,2],[0,4],[0,3,5],[2,4],[1,3,5],[2,4,6],[5,7],[6]]
print(BFS(G,0))
print(DFS(G))
G=[[1,2,3],[0,2],[0,1],[0,4,5],[3,5],[3,4]]
print(BFS(G,2))
print(DFS(G))
G=[[1,2],[0,2],[0,1],[4,5],[3,5],[3,4],[7],[6]]
print(BFS(G,4))
print(DFS(G))
G=[[2,4],[0,2],[],[],[3,6],[4],[]]
print(topological_sort(G))
G=[[1],[4,5],[0,3],[0,4],[],[4]]
print(topological_sort(G))
