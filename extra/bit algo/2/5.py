from random import randint

def FindIndex(A,p,r):
    if p>r: return False
    mid=(p+r)//2
    if A[mid]==mid: return True
    elif A[mid]<mid:
        return FindIndex(A,mid+1,r)
    return FindIndex(A,p,mid-1)

def FindIndexNatural(A):
    return A[0]==0

#testy
T1=[randint(0,40) for _ in range(20)]
T1=list(set(T1))
T1.sort()
T2=[randint(-20,20) for _ in range(20)]
T2=list(set(T2))
T2.sort()
print(*T1)
print(*T2)
print(FindIndexNatural(T1))
print(FindIndex(T2,0,len(T2)-1))
