#Implementacja Bellmana - Forda.

from math import inf

#zadanie 6
def Bellman_Ford(Gr,s):
    n=len(Gr)
    d=[inf]*n
    G=[[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(len(Gr[i])):
            G[i][Gr[i][j][0]]=Gr[i][j][1]
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

#testy
G=[[(1,3)],[(2,1),(3,5)],[(0,-2),(3,7)],[(5,-5)],[(2,-3),(3,4)],[(4,2)]]
print(Bellman_Ford(G,0))
G=[[(1,3)],[(2,1),(3,5)],[(0,-2),(3,7)],[(5,-7)],[(2,-3),(3,4)],[(4,2)]]
print(Bellman_Ford(G,3))
G=[[(1,4),(2,5)],[(3,-3),(4,11)],[(1,3),(3,2)],[(4,4)],[(2,-5)]]
print(Bellman_Ford(G,0))
G=[[(1,4),(2,5)],[(3,-3),(4,11)],[(1,3),(3,2)],[(4,4)],[(2,-2)]]
print(Bellman_Ford(G,2))
