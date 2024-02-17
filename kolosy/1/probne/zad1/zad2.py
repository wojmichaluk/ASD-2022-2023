#Wojciech Michaluk
#Algorytm najpierw sortuje przedziały niemalejąco
#względem początków (dla tych samych początków,
#ustawia przedziały nierosnąco po końcach). Potem
#zapamiętuje pozycje po tym sortowaniu i sortuje -
#po końcach niemalejąco, dla identycznych końców
#porównujemy początki. Poziom danego przedziału to
#różnica na pozycjach między 2. a 1. sortowaniem, biorę
#z tego maksimum. Szacuję złożoność obliczeniową na
#O(nlogn) z powodu używania MergeSorta (BucketSort
#przyspiesza działanie, ale nie zmienia złożoności, bo nie
#ma założenia o jednostajnym rozkładzie danych).

from zad2testy import runtests

def depth(L):
    BucketSort(L,0)
    n=len(L)
    for i in range(n):
        L[i]+=[i]
    BucketSort(L,1)
    max_level=-L[0][2]
    for i in range(1,n):
        curr_level=i-L[i][2]
        if curr_level>max_level:
            max_level=curr_level
    return max_level

def MergeSort(A,ind):
    n=len(A)
    if n>1:
        i=n//2
        L=A[:i]
        R=A[i:]
        MergeSort(L,ind)
        MergeSort(R,ind)
        j=k=0
        while j<i and k<n-i:
            if L[j][ind]<R[k][ind]:
                A[j+k]=L[j]
                j+=1
            elif L[j][ind]>R[k][ind]:
                A[j+k]=R[k]
                k+=1
            else:
                if L[j][1-ind]>R[k][1-ind]:
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

def BucketSort(A,ind):
    n=len(A)
    mi=ma=A[-1][ind]
    for i in range(1,n,2):
        if A[i-1][ind]>A[i][ind]:
            mini,maxi=A[i][ind],A[i-1][ind]
        else:
            mini,maxi=A[i-1][ind],A[i][ind]
        mi=min(mi,mini)
        ma=max(ma,maxi)
    T=[[] for _ in range(n+1)]
    for i in range(n):
        T[int(n*(A[i][ind]-mi)/(ma-mi))].append(A[i])
    k=0
    for i in range(n+1):
        MergeSort(T[i],ind)
        for j in range(len(T[i])):
            A[k]=T[i][j]
            k+=1

#złożoność w porządku, choć może nie wzorcowa
runtests( depth ) 
