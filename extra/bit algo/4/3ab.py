def lakes(G):
    n=len(G)
    A=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]=='L': A[i].append(False)
            else: A[i].append(True)
    lakes=0
    max_size=0
    for i in range(n):
        for j in range(n):
            if not A[i][j]: continue
            a=DFS(A,i,j)
            lakes+=1
            if a>max_size: max_size=a
    return lakes,max_size

def DFS(A,r,c):
    if not A[r][c]: return 0
    A[r][c]=False
    a=b=d=e=0
    if r-1>=0: a=DFS(A,r-1,c)
    if r+1<len(A): b=DFS(A,r+1,c)
    if c-1>=0: d=DFS(A,r,c-1)
    if c+1<len(A): e=DFS(A,r,c+1)
    return a+b+d+e+1

#testy
L='L'
W='W'
G=[[L,W,L,L,L,L,L,L],[L,W,L,W,W,L,L,L],
[L,L,L,W,W,L,W,L],[L,W,W,W,W,L,W,L],
[L,L,W,W,L,L,L,L],[L,W,L,L,L,L,W,W],
[W,W,L,W,W,L,W,L],[L,L,L,W,L,L,L,L]]
print(lakes(G))
