from math import inf
from queue import PriorityQueue

#zadanie 1
def Dijkstra(G,i,j):
    n=len(G)
    Gr=[[] for _ in range(100)]
    #zakładamy, że lista pięter jest posortowana
    #w przeciwnym razie for k in range(n): G[k][0].sort()
    for k in range(n):
        a=G[k]
        for l in range(len(a[0])-1):
            b=a[0][l+1]-a[0][l]
            Gr[a[0][l]].append((a[0][l+1],b*a[1]))
            Gr[a[0][l+1]].append((a[0][l],b*a[1]))
    d=[inf for _ in range(100)]
    par=[None for _ in range(100)]
    d[i]=0
    Q=PriorityQueue()
    Q.put((0,i))
    while not Q.empty():
        w,u=Q.get()
        if w==d[u]:
            for v,c in Gr[u]:
                if relax(par,d,v,c,u):
                    Q.put((d[v],v))
    return d[j],par,d

def relax(par,d,v,c,u):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

#testy
W=[([1,3,4],3),([2,3,4,5],1),([1,3,5,7],2),([1,4,5,6],4)]
print(Dijkstra(W,1,7)[0])
W=[([1,3,4,11],3),([2,5,7,9,10],2),([1,2,3,7,9,12],5),([4,5,6],4),([1,4,7,9,10],1)]
print(Dijkstra(W,2,12)[0])
W=[([1,10],6),([1,2,3,4,5],5),([3,5,7],4),([5,6],3),([6,8,10],2),([8,9,10],1)]
print(Dijkstra(W,1,10)[0])
