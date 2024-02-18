from random import randint

def find_x(A,x,i=1):
    if A[i]==None or A[i]>x:
        return binary_search(A,x,i//2,i)
    elif A[i]==x: return i
    return find_x(A,x,2*i+1)

def binary_search(A,el,p,k):
    if p>k:
        return None
    sr=(p+k)//2
    if A[sr]==None or el<A[sr]:
        return binary_search(A,el,p,sr-1)
    elif A[sr]==el:
        return sr
    return binary_search(A,el,sr+1,k)
    
#testy
T=[randint(0,100) for _ in range(0,20)]
T.sort()
T+=[None]*50
print(*T)
for i in range(0,101,10):
    print(find_x(T,i))
