from random import randint

def SinglesAndMulti(n):
    T=[0 for _ in range(10)]
    while n>0:
        T[n%10]+=1
        n//=10
    singles=multis=0
    for i in range(10):
        if T[i]==1: singles+=1
        elif T[i]>1: multis+=1
    return singles,multis

def counting_sort(T,t):
    n=len(T)
    output=[0]*n
    if t==0:
        k=T[0][2]
        for i in range(1,n):
            if T[i][2]>k: k=T[i][2]
        count=[0]*(k+1)
        for i in range(n):
            count[T[i][2]]+=1
        for i in range(1,k+1):
            count[i]+=count[i-1]
        for i in range(n-1,-1,-1):
            output[count[T[i][2]]-1]=T[i]
            count[T[i][2]]-=1
    elif t==1:
        k=T[0][1]
        for i in range(1,n):
            if T[i][1]>k: k=T[i][1]
        count=[0]*(k+1)
        for i in range(n):
            count[T[i][1]]+=1
        for i in range(k,0,-1):
            count[i-1]+=count[i]
        for i in range(n-1,-1,-1):
            output[count[T[i][1]]-1]=T[i]
            count[T[i][1]]-=1
    return output

def pretty_sort(T):
    n=len(T)
    for i in range(n):
        s,m=SinglesAndMulti(T[i])
        T[i]=(T[i],s,m)
    T=counting_sort(T,0)
    T=counting_sort(T,1)
    for i in range(n):
        T[i]=T[i][0]
    return T

#testy
T=[randint(1,10000) for _ in range(20)]
print(*T)
T=pretty_sort(T)
print(*T)
