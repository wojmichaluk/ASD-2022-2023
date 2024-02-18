#zadanie 2
def rod_cutting(x,T):
    DP=[0 for _ in range(x+1)]
    Par=[-1 for _ in range(x+1)]
    n=len(T)
    for i in range(n):
        for j in range(T[i][0],x+1):
            curr_val=DP[j-T[i][0]]+T[i][1]
            if DP[j]<curr_val:
                DP[j]=curr_val
                Par[j]=j-T[i][0]
    k=x
    cutting_points=[k]
    while Par[k]!=-1:
        cutting_points.append(Par[k])
        k=Par[k]
    lengths=[]
    for i in range(len(cutting_points)-1):
        lengths.append(cutting_points[i]-cutting_points[i+1])
    print("lengths of cut pieces:",lengths)
    return DP[x]

#testy
T=[(3,3),(1,1),(5,8),(7,12)]
print(rod_cutting(18,T))
T=[(4,6),(1,1),(9,14),(7,11),(13,21)]
print(rod_cutting(45,T))
