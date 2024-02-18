from random import randint

#zadanie 3
def SumBetween(T,_from,to):
    n=len(T)
    select(T,_from,0,n-1)
    select(T,to,_from+1,n-1)
    sum=0
    for i in range(_from,to+1):
        sum+=T[i]
    return sum

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def select(A,k,p,r):
    q=partition(A,p,r)
    if q>k:
        r=q-1
        q=partition(A,p,r)
    elif q<k:
        p=q+1
        q=partition(A,p,r)

#testy
T=[0,34,12,56,2,9,14,18]
print(SumBetween(T,2,6))
print(sum(sorted(T[2:7])))
T=[randint(-500,1500) for _ in range(1000)]
print(SumBetween(T,231,786))
print(sum(sorted(T[231:787])))
T=[randint(-100000,250000) for _ in range(100000)]
print(SumBetween(T,1267,54211))
print(sum(sorted(T[1267:54212])))
