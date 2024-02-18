#Budujemy autostradę między miastami -
#wierzchołki to miasta, krawędzie to
#autostrada. Waga krawędzi to czas budowy
#danego kawałka autostrady. Chcemy przejechać
#między wszystkimi miastami, ale też zminimalizować
#okres między otwarciem pierwszego, a ostatniego
#kawałka. Szukamy tych krawędzi. Pomysł: budujemy
#MST dla m ciągów "najcięższych" krawędzi - 
#najpierw sortujemy krawędzie, później wykonujemy 
#Kruskala i badamy różnicę między najmniejszą 
#a największą wagą.

from math import inf

#funkcje pomocnicze
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
    V=[Node(i) for i in range(n)]
    for e in E:
        u,v,w=e
        if findset(V[u])!=findset(V[v]):
            union(V[u],V[v])
            A+=[e]
    if len(A)<n-1: return A,inf
    return A,A[-1][2]-A[0][2]

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

#zadanie 4
def lowest_diff(E,n):
    m=len(E)
    MergeSort(E)
    A,a=kruskal(E,n)
    mini=a
    min_E=A
    if mini!=inf:
        for i in range(1,m):
            A,a=kruskal(E[i:],n)
            if a==inf: break
            if mini>a:
                mini=a
                min_E=A
    if mini==inf: return "not coherent"
    return mini,min_E
    
#testy
E=[(0,1,12),(0,2,5),(1,0,12),(1,2,10),(2,0,5),(2,1,10),
(2,3,20),(2,4,14),(3,2,20),(3,4,12),(3,5,1),(4,2,14),
(4,3,12),(4,6,18),(5,3,1),(5,7,7),(5,8,6),(6,4,18),(6,7,9),
(7,5,7),(7,6,9),(7,9,8),(8,5,6),(8,9,19),(9,7,8),(9,8,19)]
print(lowest_diff(E,10))
E=[(0,1,12),(0,3,11),(1,0,12),(1,2,9),(1,6,17),(2,1,9),(2,3,7),
(2,7,14),(3,0,11),(3,2,7),(3,4,15),(4,3,15),(4,5,13),(4,7,10),
(5,4,13),(5,6,20),(6,1,17),(6,5,20),(6,7,11),(7,2,14),(7,4,10),(7,6,11)]
print(lowest_diff(E,8))
E=[(0,1,1),(0,4,5),(0,5,8),(1,0,1),(1,2,3),(2,1,3),(2,3,6),(2,4,4),
(3,2,6),(3,4,2),(4,0,5),(4,2,4),(4,3,2),(4,5,7),(5,0,8),(5,4,7)]
print(lowest_diff(E,6))
E=[(0,1,11),(1,0,11),(2,3,20),(2,4,15),(2,5,13),
(3,2,20),(3,4,32),(3,5,19),(4,2,15),(4,3,32),
(4,5,21),(5,2,13),(5,3,19),(5,4,21)]
print(lowest_diff(E,6))
