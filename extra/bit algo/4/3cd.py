def lakes(G):
    n=len(G)
    A=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]=='L': A[i].append(True)
            else: A[i].append(False)
    solutions=[]
    def DFS(A,r,c,seq=[]):
        if r==c==len(A)-1:
            nonlocal solutions
            seq.append((r,c))
            solutions.append(seq)
            return True
        if not A[r][c]: return False
        A[r][c]=False
        a=b=d=e=False
        if r-1>=0: a=DFS(A,r-1,c,seq+[(r,c)])
        if r+1<len(A): b=DFS(A,r+1,c,seq+[(r,c)])
        if c-1>=0: d=DFS(A,r,c-1,seq+[(r,c)])
        if c+1<len(A): e=DFS(A,r,c+1,seq+[(r,c)])
        A[r][c]=True
        return a or b or c or d
    DFS(A,0,0)
    if len(solutions)==0: return False
    else:
        shortest=solutions[0]
        shrt_len=len(shortest)
        for i in range(1,len(solutions)):
            if len(solutions[i])<shrt_len:
                shrt_len=len(solutions[i])
                shortest=solutions[i]
        return True,shortest

#testy
L='L'
W='W'
G=[[L,W,L,L,L,L,L,L],[L,W,L,W,W,L,L,L],
[L,L,L,W,W,L,W,L],[L,W,W,W,W,L,W,L],
[L,L,W,W,L,L,L,L],[L,W,L,L,L,L,W,W],
[W,W,L,W,W,L,W,L],[L,L,L,W,L,L,L,L]]
print(lakes(G))
