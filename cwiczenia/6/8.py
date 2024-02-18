#Dany jest graf G reprezentujący mapę krajów
#z kosztami przejazdów między krajami {0,1}.
#Szukamy najtańszej drogi z kraju s do kraju t.
#Pomysł: z wierzchołka startowego próbujemy 
#dojść jak najdalej samymi zerami, jak mamy
#jedynkę to normalny BFS. Alternatywnie: 0
#wrzucamy na początek kolejki, 1 na koniec.

from queue import Queue

#zadanie 8
def cheapest_route(G,s,t):
    vis=[0]*len(G)
    par=[None]*len(G)
    d=[-1]*len(G)
    q_one=Queue()
    q_zero=Queue()
    q_one.put((s,0,None))
    while not q_one.empty():
        if not q_zero.empty(): v=q_zero.get()
        else: v=q_one.get()
        vis[v[0]]=1
        if d[v[0]]==-1: d[v[0]]=v[1]
        if par[v[0]]==None: par[v[0]]=v[2]
        for u in G[v[0]]:
            if vis[u[0]]==1: continue
            if u[1]==0: q_zero.put((u[0],d[v[0]],v[0]))
            else: q_one.put((u[0],d[v[0]]+1,v[0]))
    path=[t]
    k=t
    while par[k]!=None:
        path.append(par[k])
        k=par[k]
    return d[t],path[::-1]

#testy
G=[[(1,0),(2,0),(3,1)],[(0,0),(5,1)],[(0,0),(3,0),(5,1)],[(0,1),(2,0),(4,1)],
[(3,1),(6,0),(7,0)],[(1,1),(2,1),(6,1)],[(4,0),(5,1),(7,0)],[(4,0),(6,0)]]
print(cheapest_route(G,0,7))
print(cheapest_route(G,1,6))
G=[[(1,0),(5,1)],[(0,0),(2,1),(3,0)],[(1,1),(3,0),(6,1)],
[(1,0),(2,0),(4,1),(6,0)],[(3,1),(5,1)],[(0,1),(4,1)],[(2,1),(3,0)]]
print(cheapest_route(G,0,2))
print(cheapest_route(G,5,6))
