#Najkrótsza ścieżka w grafie, używamy BFS,
#wypisujemy ścieżkę

from queue import Queue

#zadanie 5
def spath(G,s,t):
    vis=[0]*len(G)
    par=[-1]*len(G)
    q=Queue()
    vis[s]=1
    q.put(s)
    while not q.empty():
        v=q.get()
        if v==t: break
        for u in G[v]:
            if vis[u]: continue
            par[u]=v
            q.put(u)
            vis[u]=1
    path=[t]
    k=t
    while par[k]!=-1:
        path.append(par[k])
        k=par[k]
    return path[::-1]

#testy
G=[[3,4],[3,5],[3,5],[0,1,2],[0],[1,2]]
print(*spath(G,0,5))
print(*spath(G,2,4))
G=[[1],[0,2,6],[1,3],[2,4,7],[3,5],[4],[1,7],[3,6]]
print(*spath(G,0,4))
print(*spath(G,1,7))
