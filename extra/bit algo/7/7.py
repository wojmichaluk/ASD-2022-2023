#zadanie 7
def rod_cutting2D(dims,prices,x,y):
    DP=[[0 for _ in range(x+1)] for _ in range(y+1)]
    n=len(dims)
    for i in range(n):
        for j in range(1,y+1):
            for k in range(1,x+1):
                h_val=v_val=0
                if j>=dims[i][0] and k>=dims[i][1]:
                    h_val=prices[i]+DP[dims[i][0]][k-dims[i][1]]+DP[j-dims[i][0]][k-dims[i][1]]+DP[j-dims[i][0]][dims[i][1]]
                if k>=dims[i][0] and j>=dims[i][1]:
                    v_val=prices[i]+DP[dims[i][1]][k-dims[i][0]]+DP[j-dims[i][1]][k-dims[i][0]]+DP[j-dims[i][1]][dims[i][0]]
                DP[j][k]=max(DP[j][k],h_val,v_val)
    return DP[y][x]

#testy
dims=[(1,2),(3,4),(5,6)]
prices=[3,19,43]
print(rod_cutting2D(dims,prices,12,15))
dims=[(2,6),(3,4),(1,12),(7,7)]
prices=[17,15,19,60]
print(rod_cutting2D(dims,prices,30,40))
