#Szukanie najkrótszych ścieżek w DAG - u.

from math import inf

#zadanie 2
def topo_sort(G):
    def DFSVisit(G,u):
        nonlocal to_do_list
        nonlocal visited
        visited[u]=True
        for v in G[u]:
            if not visited[v[0]]: DFSVisit(G,v[0])
        to_do_list.append(u)
    n=len(G)
    visited=[False for _ in range(n)]
    to_do_list=[]
    for i in range(n):
        if not visited[i]: DFSVisit(G,i)
    return to_do_list[::-1]

def relax(par,d,v,c,u):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

def shortest(G,s):
    V=topo_sort(G)
    n=len(G)
    d=[inf]*n
    d[s]=0
    par=[None]*n
    for i in V:
        for x,val in G[i]:
            relax(par,d,x,val,i)
    print_path(par,s,n-1)
    print()
    print_path2(par,s,n-1)
    return d,par

def print_path(parent,start,u):
    if u!=start:
        print_path(parent,start,parent[u])
    print(u,end='')

def print_path2(parent,start,u):
    T=[]
    while u!=None:
        T.append(u)
        u=parent[u]
    for i in range(len(T)-1,-1,-1):
        print(T[i],end='')
    print()

#testy
G=[[(1,2),(2,3)],[(2,-1),(3,-1)],[(4,5)],[(5,2)],[(5,-3)],[(6,3),(7,1)],[],[]]
print(shortest(G,0))
print(shortest(G,1))
G=[[(1,1),(2,3)],[(3,-1)],[(4,1),(6,-2)],[(4,2),(5,1),(6,4)],[],[],[]]
print(shortest(G,2))
print(shortest(G,1))
