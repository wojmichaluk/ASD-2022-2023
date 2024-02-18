from copy import copy

#problem plecakowy rekurencyjnie
def knapsack_rek(W,P,B,i):
    if i==0:
        if W[0]<=B: return P[0]
        return 0
    a=b=0
    a=knapsack_rek(W,P,B,i-1)
    if W[i]<=B: b=knapsack_rek(W,P,B-W[i],i-1)+P[i]
    return max(a,b)

#problem plecakowy dynamicznie
def knapsack(W,P,B):
    n=len(W)
    F=[[0 for b in range(B+1)] for _ in range(n)]
    Par=[[(-1,-1) for _ in range(B+1)] for _ in range(n)]
    for b in range(W[0],B+1):
        F[0][b]=P[0]
    for b in range(B+1):
        for i in range(1,n):
            F[i][b]=F[i-1][b]
            Par[i][b]=(i-1,b)
            if b-W[i]>=0 and F[i-1][b-W[i]]+P[i]>F[i][b]:
                F[i][b]=F[i-1][b-W[i]]+P[i]
                Par[i][b]=(i-1,b-W[i])
    return F[n-1][B],Par

#metryka Euklidesa
def d(x,y): 
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5

#TSP-przypadek ogólny
def exp_comp(C):
    n=len(C)
    S=[1 for _ in range(n)]
    def f(S,t):
        nonlocal C
        m=len(S)
        for i in range(1,m):
            if S[i]: break
        if i==m-1: return 0
        a=float('inf')
        for i in range(1,m):
            if i!=t:
                S[i]=0
                a=min(a,f(S,i)+d(C[i],C[t]))
                S[i]=1
        return a
    a=float('inf')
    for i in range(1,n):
        S=[1 for _ in range(n)]
        a=min(a,f(S,i)+d(C[i],C[0]))
    return a

#TSP-wersja bitoniczna
def bitonic(C):
    n=len(C)
    D=[[0 for _ in range(n)] for _ in range(n)]
    F=[[float('inf')]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j: D[i][j]=d(C[i],C[j])
    F[0][1]=D[0][1]
    def tspf(i,j):
        nonlocal D
        nonlocal F
        print(i,j)
        if F[i][j]!=float('inf'):
            return F[i][j]
        if i==j-1:
            best=float('inf')
            for k in range(0,j-1):
                best=min(best,tspf(k,j-1)+D[k][j])
            F[j-1][j]=best
        else:
            F[i][j]=tspf(i,j-1)+D[j-1][j]
        return F[i][j]
    a=float('inf')
    for i in range(n):
        for j in range(n):
            a=min(a,tspf(i,j))
    return a

#testy
P=[60,75,65,120,150]
W=[2,3,5,8,3]
print(knapsack_rek(W,P,6,len(P)-1))
p,par=knapsack(W,P,6)
print(p)
#print(*par,sep='\n')
P=[7,5,3]
W=[7,6,4]
print(knapsack_rek(W,P,10,len(P)-1))
p,par=knapsack(W,P,10)
print(p)
#print(*par,sep='\n')
P=[3,1,1,1,1,1]
W=[4,1,1,1,1,1]
print(knapsack_rek(W,P,5,len(P)-1))
p,par=knapsack(W,P,5)
print(p)
#print(*par,sep='\n')
#niedokończone...
#C=[(1,1),(6,1),(4,5)]
#print(exp_comp(C))
#print(bitonic(C))
