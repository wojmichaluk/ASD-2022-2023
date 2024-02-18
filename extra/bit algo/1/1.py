from random import randint

def dist(pt):
    return (pt[0]**2+pt[1]**2)**0.5

def BucketSort(A,k):
    B=[0 for _ in range(k)]
    for i in range(k):
        B[i]=[]
    n=len(A)
    for i in range(n):
        r=dist(A[i])
        if r==k: B[k-1].append(A[i])
        else: B[int((r**2)//k)].append(A[i])
    A=[]
    for i in range(k):
        InsertionSort(B[i])
        A+=B[i]
    return A

def InsertionSort(T):
    n=len(T)
    for i in range(1,n):
        el=T[i]
        x=dist(T[i])
        j=i-1
        while j>=0 and x<dist(T[j]):
            T[j+1]=T[j]
            j-=1
        T[j+1]=el

n=10
k=10
T=[]
for i in range(n):
    a=randint(-k,k)
    b=randint(-1*int((k**2-a**2)**0.5),int((k**2-a**2)**0.5))
    T.append((a,b))
print(*T[:20])
T=BucketSort(T,k)
print(*T[:20])
