#Wojciech Michaluk
#Algorytm znajduje "punkt graniczny" do którego opłaca
#się zbierać lody za pomocą metod partition oraz
#quickselect - dzięki temu wszystkie wartości większe od
#tego punktu znajdują się na dalszych pozycjach od niego.
#Punkt graniczny to indeks, dla którego jest spełnione, że
#objętość gałki jest nie mniejsza niż pozycja od końca
#tablicy ("liczba dni"), a dla poprzedniego indeksu - jeżeli
#takowy istnieje - ten warunek spełniony nie jest.  Szacuję
#złożoność czasową algorytmu na O(n), a pamięciową na
#O(1) [dodatkowej pamięci].

from kolutesty import runtests

def find_avg(A,p,r):
    ind=r
    suma=0
    for i in range(p,r+1):
        suma+=A[i]
    avg=suma/(r-p+1)
    best=abs(avg-A[ind])
    for i in range(p,r+1):
        curr=abs(avg-A[i])
        if curr<best:
            best=curr
            ind=i
    return ind

def partition(A,p,r):
    i=find_avg(A,p,r)
    A[i],A[r]=A[r],A[i]
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1
	                        
def select(A,k,p,r):
    q=partition(A,p,r)
    while q!=k:
        if q>k:
            r=q-1
        if q<k:
            p=q+1
        q=partition(A,p,r)
    return A[q]
	
def find_last(A):
    n=len(A)
    p=0
    r=n-1
    q=(p+r)//2
    diff=n-q
    val=select(A,q,p,r)
    while val!=diff:
        if val<diff:
            p=q+1
        else:
            r=q-1
        if p>r: break
        q=(p+r)//2
        diff=n-q
        val=select(A,q,p,r)
    return p

def ice_cream( T ):
    last=find_last(T)
    n=len(T)
    collected=0
    for i in range(last,n):
        collected+=T[i]-(i-last)
    return collected

# zmien all_tests na True zeby uruchomic wszystkie testy
#wzorcowy próg złożoności
runtests( ice_cream, all_tests = True )
