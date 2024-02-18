#zadanie 1
def rod_cutting(x,T):
    DP=[0 for _ in range(x+1)]
    n=len(T)
    for i in range(n):
        for j in range(T[i][0],x+1):
            DP[j]=max(DP[j],DP[j-T[i][0]]+T[i][1])
    return DP[x]

#testy
T=[(3,3),(1,1),(5,8),(7,12)]
print(rod_cutting(18,T))
T=[(4,6),(1,1),(9,14),(7,11),(13,21)]
print(rod_cutting(45,T))
