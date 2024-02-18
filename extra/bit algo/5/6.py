#zadanie 6
class Node:
    def __init__(self,value):
        self.parent=self
        self.value=value

def findset(x):
    if x.parent!=x:
        x.parent=findset(x.parent)
    return x.parent

def union(x,y):
    x=findset(x)
    y=findset(y)
    if x.value>y.value:
        x.parent=y
    else:
        y.parent=x

def strings(A,B,C):
    #zakładamy, że mamy duże litery
    #w ogólnym przypadku znajdujemy zasięg znaków
    n=len(A)
    m=len(C)
    V=[Node(i) for i in range(ord('Z')-ord('A')+1)]
    for i in range(n):
        union(V[ord(A[i])-ord('A')],V[ord(B[i])-ord('A')])
    D=[0 for _ in range(m)]
    for i in range(m):
        D[i]=chr(findset(V[ord(C[i])-ord('A')]).value+ord('A'))
    return D

#testy
print(*strings("ABDAK","FKAJD","KAJD"),sep='')
print(*strings("MAMINA","OJCIEC","WOJCIU"),sep='')
print(*strings("BANIA","CYGAN","NYGUS"),sep='')
