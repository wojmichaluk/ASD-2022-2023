#zadanie 4
class Node:
    def __init__(self,value):
        self.parent=self
        self.rank=0
        self.value=value

def findset(x):
    if x.parent!=x:
        x.parent=findset(x.parent)
    return x.parent

def union(x,y):
    x=findset(x)
    y=findset(y)
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1

def kruskal(E,n,K):
    A=[]
    MergeSort(E)
    V=[Node(i) for i in range(n)]
    for e in E:
        u,v,w=e
        if w>=K: break
        if findset(V[u])!=findset(V[v]):
            union(V[u],V[v])
            A+=[e]
    return A

def MergeSort(A):
    n=len(A)
    if n>1:
        i=n//2
        L=A[:i]
        R=A[i:]
        MergeSort(L)
        MergeSort(R)
        j=k=0
        while j<i and k<n-i:
            if L[j][2]<=R[k][2]:
                A[j+k]=L[j]
                j+=1
            else:
                A[j+k]=R[k]
                k+=1
        while j<i:
            A[j+k]=L[j]
            j+=1
        while k<n-i:
            A[j+k]=R[k]
            k+=1

def airports(E,n,K):
    A=kruskal(E,n,K)
    airps=n-len(A)
    print("Drogi do wybudowania, liczba lotnisk:")
    return A,airps

#testy
E=[(0,1,7),(0,2,4),(0,4,12),(1,0,7),(1,2,9),(2,0,4),
(2,1,9),(2,4,11),(3,5,10),(4,0,12),(4,2,11),(5,3,10)]
print(airports(E,6,12))
E=[(0,1,15),(0,2,18),(1,0,15),(1,2,11),(2,0,18),(2,1,11),
(3,4,7),(3,5,15),(4,3,7),(4,5,11),(5,3,15),(5,4,11)]
print(airports(E,6,15))
E=[(0,1,15),(0,2,11),(0,3,20),(0,4,17),(1,0,15),(1,2,19),
(1,3,21),(1,4,11),(2,0,11),(2,1,19),(2,3,14),(2,4,16),(3,0,20),
(3,1,21),(3,2,14),(3,4,18),(4,0,17),(4,1,11),(4,2,16),(4,3,18)]
print(airports(E,5,8))
