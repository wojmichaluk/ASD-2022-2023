#zadanie 4
def goodThief(A):
    n=len(A)
    DP=[0 for _ in range(n)]
    taken=[0 for _ in range(n)]
    DP[0]=A[0]
    taken[0]=1
    if A[1]>A[0]:
        DP[1]=A[1]
        taken[1]=1
    else:
        DP[1]=A[0]
    for i in range(2,n):
        if DP[i-1]>DP[i-2]+A[i]:
            DP[i]=DP[i-1]
        else:
            DP[i]=DP[i-2]+A[i]
            taken[i]=1
    tab=[]
    value_left=DP[n-1]
    for i in range(n-1,-1,-1):
        if DP[i]==value_left and taken[i]:
            tab.append(i)
            value_left-=A[i]
    tab.reverse()
    return DP[n-1],tab

#testy
A=[2,4,7,3,4,5,8,3]
print(goodThief(A))
A=[4,2,6,1,3,2,7,9]
print(goodThief(A))
A=[41,23,67,31,38,52,67,91]
print(goodThief(A))
