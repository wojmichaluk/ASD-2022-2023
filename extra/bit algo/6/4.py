#zadanie 4
def lowest_cost(A):
    m=len(A)
    n=len(A[0])
    DP=[[float('inf') for _ in range(n)] for _ in range(m)]
    DP[0][0]=A[0][0]
    for i in range(1,n):
        DP[0][i]=DP[0][i-1]+A[0][i]
    for i in range(1,m):
        DP[i][0]=DP[i-1][0]+A[i][0]
        DP[i][n-1]=DP[i-1][n-1]+A[i][n-1]
        for j in range(1,n-1):
            DP[i][j]=min(DP[i-1][j],DP[i][j-1])+A[i][j]
        for j in range(n-2,0,-1):
            DP[i][j]=min(DP[i][j],DP[i-1][j]+A[i][j],DP[i][j+1]+A[i][j])
        DP[i][0]=min(DP[i-1][0],DP[i][1])+A[i][0]
        DP[i][n-1]=min(DP[i-1][n-1],DP[i][n-2])+A[i][n-1]
    return DP[m-1][n-1]

#testy
A=[[0.5,1.7],[9.45,0.7],[1.25,2.8],[2,9.6],[3.1,2.7]]
print(lowest_cost(A))
A=[[0.05,2.6,0.7,1.13],[0.42,3.25,2.5,1],[1.13,0.16,0.24,2.8]]
print(lowest_cost(A))
A=[[0.5,2.3,3.12,1.7,0.01],[3.45,0.7,1,2.3,1],[2.13,1.76,1.24,0.3,0.46],
[2.1,3.21,0.97,4.3,2.6],[1.21,3.4,0.2,2.5,1.03],[1.2,3,2.7,4.34,2.14]]
print(lowest_cost(A))
