#zadanie 2
#dynamik - nie jest spełniony w. k.
def dynamic_change(N,c):
    n=len(N)
    DP=[float('inf') for _ in range (c+1)]
    coins_used=[[0 for _ in range(n)] for _ in range(c+1)]
    DP[0]=0
    for i in range(n):
        for j in range(N[i],c+1):
            if DP[j-N[i]]+1<DP[j]:
                DP[j]=DP[j-N[i]]+1
                coins_used[j]=coins_used[j-N[i]].copy()
                coins_used[j][i]+=1
    return DP[c],coins_used[c]

#zachłan - jest spełniony w. k.
def greedy_change(N,c):
    n=len(N)
    curr_coin_ind=n-1
    coins_used=[0 for _ in range(n)]
    left=c
    used=0
    while left:
        while left<N[curr_coin_ind]:
            curr_coin_ind-=1
        left-=N[curr_coin_ind]
        coins_used[curr_coin_ind]+=1
        used+=1
    return used,coins_used

#testy
N=[1,5,10,25,100]
print(dynamic_change(N,32))
print(greedy_change(N,32))
print('\n',dynamic_change(N,167),sep='')
print(greedy_change(N,167))
N=[1,2,7,10]
print('\n',dynamic_change(N,15),sep='')
print(dynamic_change(N,74))
