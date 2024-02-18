from math import inf
from queue import PriorityQueue

#zadanie 2
def cheapest(G,start,end,D):
    n=len(G)
    Graph=[[inf for _ in range(D+1)] for _ in range(n)]
    d=[inf for _ in range(n)]
    q=PriorityQueue()
    q.put((0,0,start))
    while not q.empty():
        c,f,v=q.get()
        if d[v]>c:
            d[v]=c
        for i in range(D+1-f):
            if c+i*G[v][1]<Graph[v][i+f]:
                Graph[v][i+f]=c+i*G[v][1]
                for u,e in G[v][0]:
                    if i+f>=e:
                        q.put((c+i*G[v][1],i+f-e,u))
    return d[end]

#testy
G=[[[(1,42),(4,35)],5.70],[[(0,42),(2,25),(4,15)],6.20],
[[(1,25),(3,31),(5,65)],6.05],[[(2,31),(5,42)],5.10],
[[(0,35),(1,15),(5,52)],5.30],[[(2,65),(3,42),(4,52)],4.90]]
print(cheapest(G,0,3,50))
G=[[[(1,5),(2,7)],8],[[(0,5),(2,3),(3,5)],5],
[[(0,7),(1,3),(3,4)],3],[[(1,5),(2,4),(4,6)],2],[[(3,6)],1]]
print(cheapest(G,0,4,6))
G=[[[(1,5),(2,7)],2],[[(0,5),(2,3),(3,5)],7],
[[(0,7),(1,3),(3,4)],9],[[(1,5),(2,4),(4,6)],4],[[(3,6)],7]]
print(cheapest(G,0,4,6))
