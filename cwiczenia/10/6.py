#Formuły logiczne - mamy formułę w CNF,
#każda zmienna w 1 nawiasie występuje
#najwyżej 2 razy. Pomysł - dwie wersje:
#1) Każdą zmienną (pozytywną) i alternatywę
#reprezentujemy wierzchołkiem, krawędź jest, 
#gdy w alternatywie występuje dana zmienna. 
#Szukamy skojarzenia, żeby do każdej alternatywy 
#była krawędź. 2) Alternatywy łączymy krawędziami
#etykietowanymi zmiennymi (jeżeli jakaś zmienna
#występuje w obu alternatywach). Szukamy,
#czy da się tak skierowac krawędzie, żeby do
#każdego wierzchołka "wchodziła" co najmniej
#jedna krawędź.

#UWAGA!!! Powyższe notatki są z zajęć, ale prawdopodobnie
#coś źle zrozumiałem :P, bo  dużo sensu nie wydają się
#one mieć. Prawidłowe podejście do tego problemu jest
#przedstawione m. in. w laboratorium nr 7 z algorytmów
#grafowych z roku 2023/2024.

from queue import Queue
from copy import deepcopy

#funkcje pomocnicze
def bipartite(G,start_v):
    colors=[-1]*len(G)
    q=Queue()
    q.put(start_v)
    colors[start_v]=0
    while not q.empty():
        v=q.get()
        for i in range(len(G)):
            if not G[v][i]: continue
            if colors[i]==-1:
                colors[i]=(colors[v]+1)%2
                q.put(i)
            else:
                if colors[i]==colors[v]: return False
    return True,colors

def FF(G,s,t):
    flow=0
    Gr=deepcopy(G)
    path=BFS(Gr,s,t)
    while path:
        w=cap(Gr,path)
        flow+=w
        update(Gr,path,w)
        path=BFS(Gr,s,t)
    return flow

def BFS(G,s,t):
    n=len(G)
    par=[None for _ in range(n)]
    visited=[False for _ in range(n)]
    q=Queue()
    q.put(s)
    visited[s]=True
    while not q.empty():
        v=q.get()
        for i in range(n):
            if G[v][i]>0 and not visited[i]:
                par[i]=v
                visited[i]=True
                q.put(i)
    k=t
    path=[]
    while k!=None:
        path.append(k)
        k=par[k]
    if len(path)<2: return None
    path.reverse()
    return path

def cap(G,path):
    minf=G[path[0]][path[1]]
    for i in range(1,len(path)-1):
        minf=min(minf,G[path[i]][path[i+1]])
    return minf

def update(G,path,w):
    for i in range(len(path)-1):
        G[path[i]][path[i+1]]-=w
        G[path[i+1]][path[i]]+=w

def max_association(G):
    a,b=bipartite(G,0)
    n=len(G)
    U=[]
    V=[]
    for i in range(n):
        if b[i]==0:
            U.append(i)
        else: V.append(i)
    G2=deepcopy(G)
    G2.append([0]*(n+2))
    G2.append([0 for _ in range(n+2)])
    for i in range(n):
        G2[i].extend([0,0])
    for u in U:
        G2[n][u]=1
    for v in V:
        G2[v][n+1]=1
    return FF(G2,n,n+1)

#zadanie 6
def CNF_sat1(no_vars,alts):
    G=[[0 for _ in range(no_vars+len(alts))] for _ in range(no_vars+len(alts))]
    for i in range(no_vars):
        for j in range(len(alts)):
            if i in alts[j]:
                G[i][j+no_vars]=1
                G[j+no_vars][i]=1
    flow=max_association(G)
    if flow<len(alts): return False
    return True

#pomocnicza do 2 wersji
def strongly_coherent(G):
    def DFSVisit(G,u,coherent=-1):
        nonlocal time
        nonlocal times
        nonlocal visited
        if coherent!=-1: coherent.append(u)
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G,v,coherent)
        time+=1
        times[u]=time
    n=len(G)
    visited=[False for _ in range(n)]
    times=[None for _ in range(n)]
    time=0
    for i in range(n):
        if not visited[i]: DFSVisit(G,i)
    T=[-1 for _ in range(n)]
    for i in range(n):
        T[n-times[i]]=i
    visited=[False for _ in range(n)]
    Gr=[[] for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            Gr[G[i][j]].append(i)
    coherent=[]
    k=0
    for i in range(n):
        if not visited[T[i]]:
            coherent.append([])
            DFSVisit(Gr,T[i],coherent[k])
            k+=1
    m=len(coherent)
    Gra=[[] for _ in range(m)]
    for i in range(m):
        for j in range(len(coherent[i])):
            u=G[coherent[i][j]]
            for v in u:
                for k in range(m):
                    if not k==i:
                        if v in coherent[k]:
                            Gra[i].append(k)
    return Gra,coherent

def CNF_sat2(no_vars,alts):
    n=len(alts)
    visited=[False for _ in range(n)]
    G=[[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            for k in alts[i]:
                for l in alts[j]:
                    if k==l:
                        if len(G[i])<len(G[j]):
                            G[i].append(j)
                            visited[j]=True
                        elif len(G[i])>len(G[j]):
                            G[j].append(i)
                            visited[i]=True
                        else:
                            if not visited[j]:
                                G[i].append(j)
                                visited[j]=True
                            else:
                                G[j].append(i)
                                visited[i]=True
    Gr,coh=strongly_coherent(G)
    m=len(coh)
    if m==1: return True
    con=[False for _ in range(m)]
    for i in range(m):
        for j in Gr[i]: con[j]=True
    for i in range(m):
        if con[i]: continue
        if len(coh[i])<2: return False
    return True

#testy
#nieprawdziwe założenia/niepełna implementacja
alts=[[0,1],[0,2,3],[1,2]]
print(CNF_sat1(4,alts))
print(CNF_sat2(4,alts))
alts=[[0,1],[0,1],[0,1]]
print(CNF_sat1(2,alts))
print(CNF_sat2(2,alts))
alts=[[0,1],[0,1],[0,1],[0,1]]
print(CNF_sat1(2,alts))
print(CNF_sat2(2,alts))
alts=[[0,1],[1,2],[0,2],[0,3,4],[3,5],[4,5]]
print(CNF_sat1(6,alts))
print(CNF_sat2(6,alts))
