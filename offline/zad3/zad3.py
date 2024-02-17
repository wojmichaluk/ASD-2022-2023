#Wojciech Michaluk
#Algorytm najpierw przepisuje odpowiednio wyrazy do tablicy
#pomocniczej (dla ustalenia uwagi: jeżeli litera na pierwszej
#pozycji jest później w alfabecie niż ostatnia, to wyraz przepisujemy
#bez zmian, jeżeli wcześniej to przepisujemy rewers - w przypadku
#tej samej litery sprawdzamy następne symetrycznie od początku i
#końca itd., palindromy przepisujemy bez zmian. Następnie sortujemy
#tę tablicę i sprawdzamy liczność najdłuższego podciągu identycznych
#wyrazów, która jest szukaną siłą napisu. Złożoność szacuję na O(N+nlogN),
#ze względu na przepisanie do tablicy pomocniczej, a następnie sortowanie
#napisów (i ich porównywanie, zależne od ich długości).

from zad3testy import runtests

def strong_string(T):
    n=len(T)
    A=[]
    for i in range(n):
        word=T[i]
        for j in range(len(word)//2):
            if ord(word[j])>ord(word[-j-1]):
                A.append(word)
                break
            elif ord(word[j])<ord(word[-j-1]):
                A.append(word[::-1])
                break
        else: A.append(word)
    m=len(A)
    MergeSort(A)
    strongest=current=1
    for i in range(1,m):
        if A[i]==A[i-1]:
            current+=1
        else:
            if current>strongest:
                strongest=current
            current=1
    return strongest

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
runtests( strong_string, all_tests=True )
