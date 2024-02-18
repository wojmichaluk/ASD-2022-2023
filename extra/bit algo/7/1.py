from zad1testy import runtests

#zadanie 1
def opt_sum(tab):
    n=len(tab)
    DP=[[0 for _ in range(n)] for _ in range(n)]
    partial_sums=[0 for _ in range(n+1)]
    for i in range(n):
        partial_sums[i+1]=partial_sums[i]+tab[i]
    for i in range(n-1):
        DP[i][i+1]=abs(tab[i]+tab[i+1])
    for i in range(2,n):
        for j in range(n-i):
            DP[j][j+i]=max(abs(partial_sums[j+i+1]-partial_sums[j]),min(DP[j+1][j+i],DP[j][j+i-1]))
    return DP[0][n-1]

#testy
A=[1,-5,2]
print(opt_sum(A))
runtests( opt_sum )
