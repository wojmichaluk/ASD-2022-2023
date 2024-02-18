#"Dobry początek" - czy w grafie skierowanym
#istnieje wierzchołek, żeby z niego była 
#ścieżka do każdego innego wierzchołka.
#Pomysł: 1) Wyznaczmy silnie spójne składowe,
#odwracamy krawędzie i szukamy potencjalnego
#kandydata wśród ujścia. 2) Bruteforce - sprawdzamy
#z każdego wierzchołka DFS, jeżeli odwiedzimy
#wszystkie wierzchołki to znaleźliśmy dobry
#początek. 3) Szukamy wierzchołka z najwyższym
#czasem przetworzenia - on jest kandydatem.
#Czas przetworzenia - post order.

#zadanie 2
#z cw 6, zad 4
def find_outlet(G):
    i=j=0
    n=len(G)
    while i<n and j<n:
        if G[i][j]==0: j+=1
        else: i+=1
    for k in range(n):
        if G[i][k]==1: return (False,None)
    for k in range(n):
        if k==i: continue
        if G[k][i]==0: return (False,None)
    return (True,i)

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
    print(Gra)
    Graf=[[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(len(Gra[i])):
            Graf[Gra[i][j]][i]=1
    a=find_outlet(Graf)
    if a[0]:
        visited=[False for _ in range(n)]
        for i in coherent[a[1]]:
            if not visited[i]:
                DFSVisit(G,i)
                if not False in visited: return True
                visited=[False for _ in range(n)]
    return False

def DFS(v,G,vis,index):
    vis[v]=index
    for x in G[v]:
        if not vis[x]:
            DFS(x,G,vis,index)

def bruteforce(G):
    vis=[0]*len(G)
    index=1
    for i in range(len(G)):
        DFS(i,G,vis,index)
        check=1
        for j in vis:
            if not j:
                check=0
                break
        if check: return True
        for k in range(len(vis)):
            vis[k]=False
    return False

def CzyDobry(G):
    vis=[0 for _ in range(len(G))]
    index=1
    for i in range(len(G)):
        if not vis[i]:
            DFS(i,G,vis,index)
            last=i
    for i in range(len(vis)):
        vis[i]=False
    DFS(last,G,vis,True)
    for i in vis:
        if not i: return i
    return True

#testy
G=[[1],[2],[0,3],[4],[5],[3]]
print(strongly_coherent(G))
print(bruteforce(G))
print(CzyDobry(G))
G=[[1],[2],[0,3,8],[4,6],[5],[3],[5],[8],[9],[5,10],[3,7]]
print(strongly_coherent(G))
print(bruteforce(G))
print(CzyDobry(G))
G=[[1],[2],[3],[1],[3,5],[3]]
print(strongly_coherent(G))
print(bruteforce(G))
print(CzyDobry(G))

G=[[1],[2],[0,3,8],[4,6],[5],[3],[5],[8],[9],[5,10],[3,7]]
strongly_coherent(G)
G=[[1],[0,2],[1,3,4],[2,5],[2,5],[3,4]]
strongly_coherent(G)
