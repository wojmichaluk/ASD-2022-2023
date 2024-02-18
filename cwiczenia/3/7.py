#Tablica k-chaotyczna - każdy element jest na swoim indeksie +-k.
#Znaleźć algorytm sortujący w czasie O(nlogk). Pomysł: budujemy
#kopiec rozmiaru k+1 zawierający początkowe elementy z tablicy.
#Następnie wykonujemy extract_min, pobieramy następny element itd.

#zadanie 7
def SortChaoticArray(A,k):
    R=[]
    n=len(A)
    k=min(k,n-1)
    T=[A[i] for i in range(k+1)]
    buildheap(T)
    for i in range(n-k-1):
        R.append(extract_min(T))
        insert(T,A[k+1+i])
    for i in range(k+1):
        R.append(extract_min(T))
    return R

def buildheap(A):
    n=len(A)
    for i in range(n//2-1,-1,-1):
        heapify_min(A,i,n)
    
def insert(T,x):
    l=len(T)
    T.append(x)
    heapify_min_up(T,l)

def heapify_min(A,i,n):
    l=2*i+1
    r=2*i+2
    min_ind=i
    if l<n and A[l]<A[min_ind]:
        min_ind=l
    if r<n and A[r]<A[min_ind]:
        min_ind=r
    if min_ind!=i:
        (A[i],A[min_ind])=(A[min_ind],A[i])
        heapify_min(A,min_ind,n)

def heapify_min_up(A,i):
    p=(i-1)//2
    if p>=0:
        if A[p]>A[i]:
            A[p],A[i]=A[i],A[p]
            heapify_min_up(A,p)

def extract_min(T):
    a=T[0]
    l=len(T)
    T[0],T[l-1]=T[l-1],T[0]
    T.pop()
    heapify_min(T,0,l-1)
    return a

#testy
T=[6,5,3,2,8,10,9]
print(*T)
T=SortChaoticArray(T,3)
print(*T)
