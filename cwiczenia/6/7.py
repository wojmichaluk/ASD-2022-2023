#Malejące krawędzie: mamy graf skierowany, każda
#krawędź ma inny koszt. Szukamy drogi s -> t, tak,
#aby każda kolejna krawędź miała mniejszy koszt. 
#Pomysł: przechodzimy BFS, zapamiętujemy koszt ostatniej
#krawędzi. Jeżeli koszt bieżącej jest mniejszy to
#idziemy dalej. Jeżeli dotrzemy do t, zwracamy True.

from queue import Queue

#zadanie 7
def decreasing_edges(G,s,t):
    vis=[0]*len(G)
    par=[None]*len(G)
    cost_to=[0]*len(G)
    q=Queue()
    vis[s]=1
    q.put((s,float('inf')))
    while not q.empty():
        v=q.get()
        for u in G[v[0]]:
            if (vis[u[0]]==1 and cost_to[u[0]]>=u[1]) or v[1]<=u[1]: continue
            par[u[0]]=v[0]
            vis[u[0]]=1
            cost_to[u[0]]=u[1]
            q.put(u)
    path=[t]
    k=t
    while par[k]!=None:
        path.append(par[k])
        k=par[k]
    if path[-1]!=s: return False,None
    return True,path[::-1]

#testy
G=[[(1,3),(3,4)],[(4,5)],[(1,1),(3,7)],[],[(2,6)]]
print(decreasing_edges(G,4,1))
print(decreasing_edges(G,0,2))
print(decreasing_edges(G,1,3))
G=[[(1,3),(2,4)],[(4,1)],[(3,7),(5,3)],
[(4,6),(5,5)],[(5,4)],[(0,2),(1,4)]]
print(decreasing_edges(G,2,0))
print(decreasing_edges(G,0,3))
print(decreasing_edges(G,2,1))
