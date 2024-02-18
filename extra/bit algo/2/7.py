from random import randint

def QuickSort(A,p,r):
    while p<r:
        q=partition(A,p,r)
        QuickSort(A,p,q-1)
        p=q+1

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def FindIfExists(A,B,C):
    QuickSort(A,0,len(A)-1)
    QuickSort(B,0,len(B)-1)
    a=0
    b=len(B)-1
    for i in range(len(C)):
        while a<len(A) and b>=0:
            if A[a]+B[b]==C[i]:
                print(A[a],B[b],C[i])
                return True
            elif A[a]+B[b]<C[i]:
                a+=1
            else: b-=1
        a=0
        b=len(B)-1
    return False

#testy
A=[randint(1,100) for _ in range(20)]
B=[randint(1,100) for _ in range(20)]
C=[randint(1,100) for _ in range(20)]
print(*A)
print(*B)
print(*C)
print(FindIfExists(A,B,C))
