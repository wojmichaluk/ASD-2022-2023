#zadanie 4
def Pascal(S,P):
    n=len(S)
    k=len(S[0])
    DP=[[0 for _ in range(P)] for _ in range(n)]
    SP=[[S[i][j] for j in range(k)] for i in range(n)]
    for i in range(n):
        for j in range(1,k):
            SP[i][j]+=SP[i][j-1]
    for i in range(P):
        if i>=k: DP[0][i]=DP[0][i-1]
        else: DP[0][i]=SP[0][i]
    for i in range(1,n):
        for j in range(P):
            if j>=k:
                DP[i][j]=DP[i-1][j]
                for l in range(1,k+1):
                    DP[i][j]=max(DP[i][j],DP[i-1][j-l]+SP[i][l-1])
            else:
                DP[i][j]=max(SP[i][j],DP[i-1][j])
                for l in range(1,j+1):
                    DP[i][j]=max(DP[i][j],DP[i-1][j-l]+SP[i][l-1])
    print(DP)
    return DP[n-1][P-1]     

#testy
S=[[1,0,2],[2,-1,1],[1,0,3]]
print(Pascal(S,4))
S=[[2,-1,2,0,3],[-2,1,3,1,2],[3,0,1,0,-1],[0,-3,4,2,-1],[1,1,1,1,2]]
print(Pascal(S,8))
