from random import randint

def counting_sort(T,k):
    n=len(T)
    output=[0]*n
    count=[0]*k
    for i in range(n):
        count[T[i]]+=1
    for i in range(1,k):
        count[i]+=count[i-1]
    for i in range(n-1,-1,-1):
        output[count[T[i]]-1]=T[i]
        count[T[i]]-=1
    return output

def bubble_sort(T):
    n=len(T)
    for i in range(n):
        for j in range(1,n-i):
            if T[j-1]>T[j]:
                T[j],T[j-1]=T[j-1],T[j]

n=1000000
k=10000000
A=[]
T=[randint(0,k) for _ in range(n)]
for i in range(10):
    j=randint(0,n-1)
    while j in A:
        j=randint(0,n-1)
    A.append(j)
    if i%2==0:
        T[j]=randint(-100,-20)
    else:
        T[j]=randint(k+100,k+500)
A=[0 for _ in range(10)]
counter=0
for i in range(n):
    if counter==10: break
    if T[i]>k or T[i]<0:
        A[counter]=T[i]
        T=T[:i]+T[i+1:]
        counter+=1
T=counting_sort(T,k)
bubble_sort(A)
i=0
while i<10:
    if A[i]>k: break
    i+=1
T=A[:i]+T+A[i:]
print(*T[:20])
