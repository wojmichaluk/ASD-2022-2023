#Implementacja algorytmu Kruskala - 
#wykorzystujemy sort i find / union.

#zadanie 2
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

def kruskal(E,n):
    A=[]
    MergeSort(E)
    V=[Node(i) for i in range(n)]
    for e in E:
        u,v,w=e
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

#testy
E=[(0,1,1),(0,4,5),(0,5,8),(1,0,1),(1,2,3),(2,1,3),(2,3,6),(2,4,4),
(3,2,6),(3,4,2),(4,0,5),(4,2,4),(4,3,2),(4,5,7),(5,0,8),(5,4,7)]
print(kruskal(E,6))
E=[(0,1,12),(0,3,11),(1,0,12),(1,2,9),(1,6,17),(2,1,9),(2,3,7),
(2,7,14),(3,0,11),(3,2,7),(3,4,15),(4,3,15),(4,5,13),(4,7,10),
(5,4,13),(5,6,20),(6,1,17),(6,5,20),(6,7,11),(7,2,14),(7,4,10),(7,6,11)]
print(kruskal(E,8))
E=[(0,1,11),(0,5,13),(1,0,11),(1,2,20),(1,6,17),(2,1,20),
(2,3,17),(3,2,17),(3,4,32),(4,3,32),(4,5,21),(5,0,13),
(5,4,21),(5,6,11),(6,1,17),(6,5,11),(6,7,4),(7,6,4)]
print(kruskal(E,8))
