from queue import Queue

def BFS(s,G):
    n=len(G)
    visited=[-1]*n
    q=Queue()
    q.put((s,0))
    while not q.empty():
        v,w=q.get()
        visited[v]=w
        print(*visited)
        for u in G[v]:
            if visited[u]==-1:
                q.put((u,w+1))
                visited[u]=w+1

def DFS1(v,G):
    n=len(G)
    visited=[False]*n
    def wew(v,G):
        nonlocal visited
        visited[v]=True
        print(*visited)
        for neigh in G[v]:
            if not visited[neigh]:
                wew(neigh,G)
    wew(v,G)

def DFS2(v,G):
    n=len(G)
    visited=[False]*n
    Stack=[v]
    while len(Stack)!=0:
        u=Stack[-1]
        visited[u]=True
        print(*visited)
        Stack.pop()
        for w in G[u]:
            if not visited[w]:
                Stack.append(w)

#testy
G=[[1,2],[0,2,3,4],[0,1,4,5,6],[1,6],[1,2,5],[2,4],[2,3]]
BFS(0,G)
print()
DFS1(0,G)
print()
DFS2(0,G)
