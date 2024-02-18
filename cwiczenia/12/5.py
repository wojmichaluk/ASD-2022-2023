#Dana jest szachownica o wymiarach n x n.
#Elementy to liczby wymierne. Należy dojść
#z lewego górnego rogu do prawego dolnego rogu
#ruchami wieży o jedno pole, tylko w dół lub
#w prawo.

#zadanie 5
def rek(A,i,j): #rekurencyjnie
    if i==j==0: return A[0][0]
    if i==0: return A[i][j]+rek(A,i,j-1)
    if j==0: return A[i][j]+rek(A,i-1,j)
    return min(rek(A,i-1,j),rek(A,i,j-1))+A[i][j]

def lowest_cost(A): #iteracyjnie
    n=len(A)
    DP=[[0 for _ in range(n)] for _ in range(n)]
    DP[0][0]=A[0][0]
    for i in range(1,n):
        DP[i][0]=DP[i-1][0]+A[i][0]
    for i in range(1,n):
        DP[0][i]=DP[0][i-1]+A[0][i]
    for i in range(1,n):
        for j in range(1,n):
            DP[i][j]=min(DP[i-1][j],DP[i][j-1])+A[i][j]
    return DP[n-1][n-1]

#testy
A=[[0.5,2.3,-1.7,0.01],[-1.12,3.45,0.7,-1],[2.13,-1.24,2.8,0.3],[2,1.1,4.-3,2.6]]
print(lowest_cost(A))
print(rek(A,len(A)-1,len(A)-1))
A=[[0.05,2.6,-0.7],[0.42,3.25,1],[1.13,-0.24,2.8]]
print(lowest_cost(A))
print(rek(A,len(A)-1,len(A)-1))
A=[[0.5,-2.3,-3.12,0.56,-1.7,0.01],[1.12,-3.45,-0.7,1,-2.3,1],[-2.13,1.76,-1.24,2.8,-0.3,0.46],
[2.1,-0.1,-3.21,0.97,-4.3,2.6],[-1.21,3.4,-0.2,5.01,-2.5,1.03],[0.01,-1.2,3,-2.7,4.34,-2.14]]
print(lowest_cost(A))
print(rek(A,len(A)-1,len(A)-1))
