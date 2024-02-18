#Checemy znaleźć "najkrótszą" ścieżkę - 
#o najmniejszym możliwym iloczynie wag.
#Pomysł: zamiast liczyć a*b*c*d, liczymy
#log(abcd) = loga + logb + logc + logd.
#uwaga na wagi e < 1 (loge < 0) - trzeba
#użyć algorytmu Bellmana - Forda.

from math import inf
from math import log

#zadanie 3
def Bellman_Ford(Gr,s): #modyfikacja z zadania 6
    n=len(Gr)
    d=[inf]*n
    G=[[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(len(Gr[i])):
            G[i][Gr[i][j][0]]=log(Gr[i][j][1])
    d[s]=0
    par=[None]*n
    for i in range(n):
        B=False
        for j in range(n):
            for k in range(n):
                B|=relax(par,d,j,k,G)
    if B: return d,par,False
    return d,par,True

def relax(par,d,i,j,G):
    if d[j]>d[i]+G[i][j]:
        d[j]=d[i]+G[i][j]
        par[j]=i
        return True
    return False

def path(G,start_v,end_v):
    a=Bellman_Ford(G,start_v)
    if not a[2]: return a[0],a[1],"no path - negative cycle"
    k=end_v
    p=[]
    while k!=None:
        p.append(k)
        k=a[1][k]
    if p[-1]!=start_v:
        return a[0],a[1],"no path in this directed graph"
    p.reverse()
    return a[0],a[1],p

#testy
G=[[(1,5),(2,9)],[(2,1),(3,5)],[(3,0.7)],[(5,7)],[(2,0.13),(3,4)],[(4,12)]]
print(path(G,2,1))
G=[[(1,5)],[(2,1),(3,5)],[(0,9),(3,0.7)],[(5,7)],[(2,0.13),(3,4)],[(4,12)]]
print(path(G,0,4))
G=[[(1,5),(2,9)],[(2,1),(3,5)],[(3,0.7)],[(5,2)],[(2,0.13),(3,4)],[(4,0.12)]]
print(path(G,0,5))
