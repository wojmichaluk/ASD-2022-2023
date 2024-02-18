from queue import Queue

def BFS(s,G):
    n=len(G)
    visited=[-1]*n
    q=Queue()
    q.put((s,0))
    while not q.empty():
        v,w=q.get()
        visited[v]=w
        for u in G[v]:
            if visited[u]!=-1 and visited[u]==w-1: continue
            if visited[u]==-1:
                q.put((u,w+1))
                visited[u]=w+1
            else: return True
    return False

#testy
G=[[1,2],[0,2,3,4],[0,1,4,5,6],[1,6],[1,2,5],[2,4],[2,3]]
print(BFS(0,G))
G=[[1,2,3],[0,4,6],[0,7],[0,10],[1,5],
[4],[1],[2,8,9],[7],[7],[3,11],[10]]
print(BFS(0,G))
