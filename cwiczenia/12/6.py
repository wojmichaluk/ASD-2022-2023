#Mamy tablicę reprezentującą szufladę
#z pieniędzmi (i informację, jakie są
#nominały). Szukamy minimalnej liczby
#monet do wydania reszty.

from math import ceil

#zadanie 6
def minimum_no_coins_rek(N,R): #rekurencyjnie
    n=len(N)
    N_gr=[int(1000*N[i])//10 for i in range(n)]
    R_gr=int(1000*R)//10
    return rek(N_gr,R_gr)

def rek(N,R,c=0,i=0):
    if R==0: return c
    if i==len(N) or R<0: return float('inf')
    return min(rek(N,R,c,i+1),rek(N,R-N[i],c+1,i+1),rek(N,R-N[i],c+1,i))

def minimum_no_coins(N,R): #dynamicznie
    n=len(N)
    N_gr=[int(1000*N[i])//10 for i in range(n)]
    R_gr=int(1000*R)//10
    DP=[[float('inf') for _ in range(R_gr+1)] for _ in range(n+1)]
    for i in range(n+1):
        DP[i][0]=0
    for i in range(1,n+1):
        for j in range(R_gr+1):
            DP[i][j]=DP[i-1][j]
            if j>=N_gr[i-1]: DP[i][j]=min(DP[i][j],DP[i][j-N_gr[i-1]]+1)
    return DP[n][R_gr]

#testy
N=[0.1,0.2,0.5,1,2,5]
print(minimum_no_coins(N,10.65))
print(minimum_no_coins(N,8.5))
print(minimum_no_coins(N,100.7))
print(minimum_no_coins_rek(N,10.65))
print(minimum_no_coins_rek(N,8.5),'\ntoo long!')
#print(minimum_no_coins_rek(N,100.7))
N=[0.12,0.27,0.52,1.46,2.53]
print(minimum_no_coins(N,7.6))
print(minimum_no_coins(N,4.9))
print(minimum_no_coins(N,10.73))
print(minimum_no_coins_rek(N,7.6))
print(minimum_no_coins_rek(N,4.9))
print(minimum_no_coins_rek(N,10.73))
