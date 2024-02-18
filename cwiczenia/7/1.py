#Ścieżka Hamiltona w DAG.
#Pomysł: sortujemy graf topologicznie, sprawdzamy czy jest 
#krawędź pomiędzy i - tym a i+1 - ym wierzchołkiem.

#zadanie1
def Hamil(G):
    A=[]
    vis=[0]*len(G)
    for i in range(len(G)):
        if not vis[i]:
            DFS(i,G,vis,A)
    A.reverse()
    for i in range(len(G)-1):
        u,v=A[i],A[i+1]
        if not v in G[u]: return False
    return True

def DFS(v,G,vis,A):
    vis[v]=1
    for x in G[v]:
        if not vis[x]:
            DFS(x,G,vis,A)
    A.append(v)

#testy
G=[[1],[2],[0,3],[4],[5],[3]]
print(Hamil(G))
G=[[1],[2],[3],[1],[3,5],[3]]
print(Hamil(G))
