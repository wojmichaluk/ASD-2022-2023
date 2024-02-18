#zadanie 3
def amazon_stairs(A):
    n=len(A)
    DP=[0 for _ in range(n)]
    DP[0]=1
    for i in range(n-1):
        for j in range(1,A[i]+1):
            if i+j>=n: break
            DP[i+j]+=DP[i]
    return DP[n-1]

#testy
A=[1,3,2,1,0]
print(amazon_stairs(A))
A=[1,1,1,1,1,1,1,1,1,0]
print(amazon_stairs(A))
A=[10,9,8,7,6,5,4,3,2,1,0]
print(amazon_stairs(A))
