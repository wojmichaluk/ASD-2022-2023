def diameter(v,G):
    n=len(G[v])
    if n==0: return 0
    A=[0 for _ in range(n)]
    for i in range(n):
        DFS1(G[v][i],G,A,i)
    if n==1: return A[0]
    suma=0
    for i in range(n):
        for j in range(i+1,n):
            if A[i]+A[j]>suma: suma=A[i]+A[j]
    return suma

def DFS1(v,G,A,i):
    n=len(G)
    visited=[False]*n
    Stack=[(v,1)]
    while len(Stack)!=0:
        u,t=Stack[-1]
        visited[u]=True
        Stack.pop()
        if len(G[u])==0:
            A[i]=max(A[i],t)
        for w in G[u]:
            if not visited[w]:
                Stack.append((w,t+1))

def DFS2(v,G):
    n=len(G)
    visited=[False]*n
    max_dist=0
    max_v=v
    Stack=[(v,0)]
    while len(Stack)!=0:
        u,t=Stack[-1]
        visited[u]=True
        Stack.pop()
        if len(G[u])==1:
            if max_dist<t:
                max_dist=t
                max_v=u
        for w in G[u]:
            if not visited[w]:
                Stack.append((w,t+1))
    print(max_v)
    return max_v,max_dist

#testy
G=[[1,3,4],[2],[],[],[5,6,7,8],[],[],[],[]] 
print(diameter(0,G)) #1.1
G=[[1,3,4],[0,2],[1],[0],[0,5,6,7,8],[4],[4],[4],[4]] 
a=DFS2(0,G)
print(DFS2(a[0],G)[1]) #1.2
G=[[1,2,3],[4,6],[7],[10],[5],[],[],[8,9],[],[],[11,12],[],[]]
print(diameter(0,G)) #2.1
G=[[1,2,3],[0,4,6],[0,7],[0,10],[1,5],[4],[1],[2,8,9],[7],[7],[3,11,12],[10],[10]]
a=DFS2(0,G)
print(DFS2(a[0],G)[1]) #2.2
G=[[1,2,3],[0,4,6],[0,7],[0,10],[1,5],[4],[1],[2,8,9],
[7],[7],[3,11,12],[10,13],[10,14],[11],[12]]
a=DFS2(0,G)
print(DFS2(a[0],G)[1]) #3.2
