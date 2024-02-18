from queue import Queue

def BFS(s,G):
    n=len(G)
    visited=[-1]*n
    days=[]
    q=Queue()
    q.put((s,0))
    while not q.empty():
        v,w=q.get()
        if len(days)<=w: days.append(1)
        else: days[w]+=1
        visited[v]=w
        for u in G[v]:
            if visited[u]==-1:
                q.put((u,w+1))
                visited[u]=w+1
    max_ind=0
    max_val=days[0]
    for i in range(1,len(days)):
        if days[i]>max_val:
            max_val=days[i]
            max_ind=i
    return max_ind,max_val

#testy
G=[[1,2],[0,2,3,4],[0,1,4,5,6],[1,6],[1,2,5],[2,4],[2,3]]
print(BFS(0,G))
G=[[1,2,3],[0,4,6],[0,7],[0,10],[1,5],[4],
[1],[2,8,9],[7],[7],[3,11,12],[10],[10]]
print(BFS(0,G))
