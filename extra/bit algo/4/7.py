from queue import Queue

def BFS(A):
    S=[]
    n=len(A)
    visited=[-1]*n
    for i in range(n):
        if A[i][0]=='S':
            S.append(A[i][1])
            visited[i]=0
    q=Queue()
    for i in range(len(S)):
        for j in range(len(S[i])):
            q.put((S[i][j],1))
    while not q.empty():
        v,w=q.get()
        if visited[v]==-1 or visited[v]>w: visited[v]=w
        for u in G[v][1]:
            if visited[u]==-1:
                q.put((u,w+1))
                visited[u]=w+1
    return visited
                
#testy
G=[('D',[1]),('D',[0,2,3]),('D',[1,3]),('S',[1,2,4]),('D',[3,5]),
('S',[4,6]),('D',[5,7,8]),('D',[6,8,9]),('D',[6,7]),('D',[7])]
print(*BFS(G))
G=[('D',[1,4]),('D',[0,2]),('D',[1,3]),('D',[2,4,5]),('S',[0,3,6,9]),
('D',[3,6]),('S',[4,5,7]),('D',[6,8]),('D',[7,9]),('D',[4,8])]
print(*BFS(G))
