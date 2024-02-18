#Mamy ciąg A0,A1,...,A n-1. Chcemy go
#podzielić na k<n podciągów spójnych
#tak, aby maksymalna z sum była możliwie
#najmniejsza. Pomysł: A - ciąg wejściowy,
#f(i,j,m) - największa suma fragmentu
#w optymalnym podziale ciągu A od indeksu
#i do indeksu j na m fragmentów.

from random import randint

#zad 7
def min_of_maxes_rek(A,m):
    sums=[0 for _ in range(m)]
    return rek(A,sums)

def rek(A,sums,i=0,j=0):
    if j==len(A): return max(sums)
    temp=sums[:i]+[sums[i]+A[j]]+sums[i+1:]
    if i==len(sums)-1: return rek(A,temp,i,j+1)
    a=rek(A,temp,i,j+1)
    b=rek(A,temp,i+1,j+1)
    c=rek(A,sums,i+1,j)
    return min(a,b,c)

def calc(A,DP,i,j,m):
    if DP[i][j][m]==float('inf'):
        DP[i][j][m]=DP[i][j][m-1]
        for k in range(m):
            l=m-k-1
            for p in range(i,j):
                DP[i][j][m]=min(DP[i][j][m],max(calc(A,DP,i,p,k),calc(A,DP,p+1,j,l)))
    return DP[i][j][m]
            
def min_of_maxes(A,m):
    n=len(A)
    partial_sums=[0 for _ in range(n+1)]
    for i in range(1,n+1):
        partial_sums[i]=partial_sums[i-1]+A[i-1]
    DP=[[[float('inf') for _ in range(m)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            DP[i][j][0]=partial_sums[j+1]-partial_sums[i]
        for k in range(1,m):
            DP[i][i][k]=A[i]
    return calc(A,DP,0,n-1,m-1)

#testy
A=[1,2,3,4]
print(A)
print(min_of_maxes_rek(A,3))
print(min_of_maxes(A,3))
A=[0,3,7,8,12,3,4,-5]
print(A)
print(min_of_maxes_rek(A,3))
print(min_of_maxes(A,3))
A=[randint(-25,100) for _ in range(10)]
print(A)
print(min_of_maxes_rek(A,5))
print(min_of_maxes(A,5))
