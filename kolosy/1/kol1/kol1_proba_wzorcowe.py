#Wojciech Michaluk
#Algorytm najpierw bierze początkowe p elementów
#tablicy, następnie je sortuje niemalejąco i rozdziela do
#dwóch kolejek priorytetowych (elementy większe od
#k-tego największego ułożone rosnąco, elementy mniejsze
# - malejąco). W każdym kroku przechodzimy po tablicy T i
#badamy kolejny element, umieszczając go w odpowiedniej
#kolejce i dodając do sumy k-ty największy element z
#przedziału. Jeżeli element jest spoza "okna", to zostaje
#pobrany następny. Szacuję złożoność czasową algorytmu
#na O(nlogn), a pamięciową na O(nlogn).

from kol1testy import runtests
from queue import PriorityQueue

def ksum(T, k, p):
    A=[(T[i],i) for i in range(p)]
    MergeSort(A)
    suma=A[-k][0]
    a1=A[-k][0]
    b1=A[-k][1]
    q1=PriorityQueue()
    q2=PriorityQueue()
    for i in range(p-k,p):
        q1.put(A[i])
    for i in range(p-k):
        q2.put((-A[i][0],A[i][1]))
    n=len(T)
    for i in range(p,n):
        suma+=a1
        el1=T[i-p]
        el2=T[i]
        if el1>=a1:
            q1.put((a1,b1))
            if el2>=a1:
                q1.put((el2,i))
            else:
                a2,b2=q2.get()
                while b2<i-p:
                    a2,b2=q2.get()
                if el2>-a2:
                    q1.put((el2,i))
                    q2.put((a2,b2))
                else:
                    q1.put((-a2,b2))
                    q2.put((-el2,i))
        else:
            q2.put((-a1,b1))
            a1,b1=q1.get()
            while b1<i-p:
                a1,b1=q1.get()
            q1.put((a1,b1))
            if el2>=a1:
                q1.put((el2,i))
            else:
                a2,b2=q2.get()
                while b2<i-p:
                    a2,b2=q2.get()
                if el2>-a2:
                    q1.put((el2,i))
                    q2.put((a2,b2))
                else:
                    q1.put((-a2,b2))
                    q2.put((-el2,i))
        a1,b1=q1.get()
        while b1<i-p:
            a1,b1=q1.get()
    return suma      

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
            if L[j]<=R[k]:
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

# zmien all_tests na True zeby uruchomic wszystkie testy
#błędy w implementacji
runtests( ksum, all_tests=True )
