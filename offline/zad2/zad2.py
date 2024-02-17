#Wojciech Michaluk
#Algorytm wykorzystuje sortowanie kopcowe, częściowo sortuje tablicę
#(znajduje największe wartości do pewnego momentu). Ten moment
#następuje, gdy ilość śniegu jest nie większa niż ilość dni, które upłynęły -
#oznacza to, że cały śnieg już by stopniał, więc dalej nie opłaca się szukać.
#Rozumowanie jest poprawne, bo dążymy do zebrania śniegu z pól, gdzie
#jest go najwięcej, a uwzględniając warunki zadania, istnieje taka "ścieżka",
#żeby je wszystkie zebrać (niekoniecznie zaczynając od największego).
#Złożoność algorytmu szacuję na nlogn - sortowanie kopcowe, ale w
#korzystnym przypadku może dążyć nawet do złożoności liniowej.

from zad2testy import runtests

def snow( S ):
    #wykorzystanie sortowania kopcowego
    n=len(S)
    for i in range(n//2-1,-1,-1):
        heapify(S,i,n)
    collected=0
    for i in range(n-1,0,-1):
        (S[0],S[i])=(S[i],S[0])
        if not(S[i]>n-1-i):
            break
        collected+=S[i]-n+i+1
        heapify(S,0,i)
    return collected

def heapify(A,i,n):
    l=2*i+1
    r=2*i+2
    max_ind=i
    if l<n and A[l]>A[max_ind]:
        max_ind=l
    if r<n and A[r]>A[max_ind]:
        max_ind=r
    if max_ind!=i:
        (A[i],A[max_ind])=(A[max_ind],A[i])
        heapify(A,max_ind,n)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
