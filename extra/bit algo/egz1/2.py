#zadanie 2
def kintersect(A,k):
    n=len(A)
    DP=[[None for _ in range(k+1)] for _ in range(n)]
    par=[[None for _ in range(k+1)] for _ in range(n)]
    for i in range(n):
        DP[i][0]=(0,0)
        DP[i][1]=A[i]
        par[i][0]=(-1,-1)
        par[i][1]=(i,0)
        for j in range(1,k+1):
            if i<j-1: 
                DP[i][j]=(0,0)
                par[i][j]=(-1,-1)
    for i in range(n):
        for j in range(2,k+1):
            best_int=(0,0)
            best_len=-1
            best_par=(-1,-1)
            for m in range(i):
                curr_int=intersect(A[i],DP[m][j-1])
                curr_len=curr_int[1]-curr_int[0]
                if curr_len>best_len:
                    best_int=curr_int
                    best_len=curr_len
                    best_par=(m,j-1)
            DP[i][j]=best_int
            par[i][j]=best_par
    max_klen=DP[k-1][k][1]-DP[k-1][k][0]
    best_ind=k-1
    for i in range(k,n):
        curr_klen=DP[i][k][1]-DP[i][k][0]
        if curr_klen>max_klen:
            max_klen=curr_klen
            best_ind=i
    chosen=[best_ind]
    t=par[best_ind][k]
    while par[t[0]][t[1]]!=(-1,-1):
        chosen.append(t[0])
        t=par[t[0]][t[1]]
    chosen.reverse()
    return chosen
    
def intersect(A,B):
    a=max(A[0],B[0])
    b=min(A[1],B[1])
    if a>=b: return (0,0)
    return (a,b)

#testy
A=[(0,4),(1,10),(6,7),(2,8)]
print(kintersect(A,3))
print(kintersect(A,2))
A=[(-6,10),(3,7),(1,9),(2,6),(-3,7),(5,12),(0,14),(-1,11),(1,13),(2,15),(-4,6)]
print(kintersect(A,6))
print(kintersect(A,4))
A=[(1,18),(2,17),(3,16),(4,15),(5,14)]
print(kintersect(A,4))
print(kintersect(A,3))
A=[(3,7),(1,9),(2,6),(-3,7),(5,12),(0,14),(-1,11),(1,13),(2,15),(-4,6)]
print(kintersect(A,6))
print(kintersect(A,4))
A=[(1,18),(2,17),(3,16),(4,15),(5,14)]
print(kintersect(A,4))
print(kintersect(A,3))
