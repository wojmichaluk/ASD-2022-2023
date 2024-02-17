#Wojciech Michaluk
#Algorytm najpierw bierze początkowe p elementów
#tablicy, następnie je sortuje niemalejąco i dodaje do sumy
#k-ty element od końca. Następnie przesuwa się po pozostałych
#elementach tablicy, w każdym kroku wyrzucając element,
#który "wypadł" z przedziału i wstawiając nowy oraz po tych
#operacjach dodaje do sumy k-ty element od końca itd.
#Szacuję złożoność czasową algorytmu na O(np), a złożoność
#pamięciową na O(p) - algorytm używa pomocniczej tablicy
#rozmiaru p.

from kol1testy import runtests

def ksum(T, k, p):
    n=len(T)
    A=[(T[i],i) for i in range(p)]
    MergeSort(A)
    suma=A[-k][0]   
    for i in range(p,n):
        for j in range(p):
            if A[j][1]==i-p:
                A=A[:j]+A[j+1:]
                break
        j=0
        while j<p-1 and A[j][0]<=T[i]:
            j+=1
        A=A[:j]+[(T[i],i)]+A[j:]
        suma+=A[-k][0]
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
#kod poprawny, pierwszy próg złożoności
runtests( ksum, all_tests=True )
