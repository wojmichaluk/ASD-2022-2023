#Liczenie inwersji w tablicy

from random import randint

#zadanie2
def Inversions(A):
    return merge_count_inversion(A)[1]

def merge_count_inversion(A):
    if len(A)<2:
        return A,0
    mid=len(A)//2
    left,a=merge_count_inversion(A[:mid])
    right,b=merge_count_inversion(A[mid:])
    result,c=merge_sort(left,right)
    return result,a+b+c
    
def merge_sort(L,R):
    ll=len(L)
    rl=len(R)
    A=[0 for _ in range(ll+rl)]
    inv=0
    i=j=0
    while i<ll and j<rl:
        if L[i]<=R[j]:
            A[i+j]=L[i]
            i+=1
        else:
            A[i+j]=R[j]
            inv+=ll-i
            j+=1
    while i<ll:
        A[i+j]=L[i]
        i+=1
    while j<rl:
        A[i+j]=R[j]
        j+=1
    return A,inv

#testy
T=[randint(1,10) for _ in range(10)]
print(*T)
print(Inversions(T))
T=[1,5,2,6,10,3]
print(*T)
print(Inversions(T))
