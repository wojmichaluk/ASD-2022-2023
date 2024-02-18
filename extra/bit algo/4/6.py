def DFS(v,G,A):
    A[v]+=1
    if len(G[v])==0:
        return 1
    for neigh in G[v]:
        a=DFS(neigh,G,A)
        A[v]+=a
    return A[v]

#testy
G=[[1,3,4],[2],[],[],[5,6,7,8],[],[],[],[]]
A=[0 for _ in range(len(G))]
DFS(0,G,A)
print(*A)
G=[[1,2,3],[4,6],[7],[10],[5],[],[],[8,9],[],[],[11,12],[],[]]
A=[0 for _ in range(len(G))]
DFS(0,G,A)
print(*A)
