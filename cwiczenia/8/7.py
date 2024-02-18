#Chcemy znaleźć optymalną ścieżkę z start do
#end, aby miała krawędzie o malejących wagach.

from math import inf
from queue import PriorityQueue

#zadanie 7
def Dijkstra(G,start,end):
    n=len(G)
    for i in range(n):
        MergeSort(G[i])
    d=[inf for _ in range(n)]
    par=[None for _ in range(n)]
    d[start]=0
    Q=PriorityQueue()
    Q.put((0,start,inf))
    while not Q.empty():
        w,u,z=Q.get()
        if w==d[u]:
            for v,c in G[u]:
                if c<z and relax(par,d,v,c,u):
                    Q.put((d[v],v,c))
    t=end
    path=[]
    while t!=None:
        path.append(t)
        t=par[t]
    if path[-1]!=start:
        return d[end],"no path satisfying given criteria"
    path.reverse()
    return d[end],path

def relax(par,d,v,c,u):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

def MergeSort(A):
    n=len(A)
    if n>1:
        i=n//2
        L=A[:i]
        R=A[i:]
        MergeSort(L)
        MergeSort(R)
        j=k=0
        while j<i and k<n-i:
            if L[j][1]<=R[k][1]:
                A[j+k]=L[j]
                j+=1
            else:
                A[j+k]=R[k]
                k+=1
        while j<i:
            A[j+k]=L[j]
            j+=1
        while k<n-i:
            A[j+k]=R[k]
            k+=1

#testy
G=[[(1,11),(2,15),(5,25)],[(0,11),(3,19),(4,12)],
[(0,15),(3,13),(4,17)],[(1,19),(2,13),(4,11),(5,15)],
[(1,12),(2,17),(3,11),(5,18)],[(0,25),(3,15),(4,18)]]
print(Dijkstra(G,0,4))
print(Dijkstra(G,1,2))
G=[[(4,120),(6,92)],[(2,21),(6,79)],[(1,21),(3,24),(5,19)],
[(2,24),(4,95),(6,15)],[(0,120),(3,95)],
[(2,19),(6,17)],[(0,92),(1,79),(3,15),(5,17)]]
print(Dijkstra(G,1,3))
print(Dijkstra(G,0,2))
G=[[(1,17),(3,25)],[(0,17),(2,19)],[(1,19),(3,28)],[(0,25),(2,28)]]
print(Dijkstra(G,0,2))
