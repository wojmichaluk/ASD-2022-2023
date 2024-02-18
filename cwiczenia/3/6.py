#Struktura danych z operacjami insert, extract_median.
#Operacje mają być w złożoności O(logn). Pomysł:
#mamy dwa kopce i środkowy element x. Kopiec z elementami
#mniejszymi od x to max_heap, a kopiec z elementami
#większymi od x to min_heap. Mediana to element środkowy
#lub (max z kopca min + min z kopca max) / 2, jeżeli środek
#jest pusty. Wstawianie: jeżeli środek jest pusty, to
#porównujemy z elementami skrajnymi z kopców. Jeżeli nie,
#to po wstawieniu usuwamy element ze środka.

from random import randint

#zadanie 6
class Heap:
    def __init__(self):
        self.Tmax=[]
        self.Tmin=[]
        self.median=None
        self.size=0

def insert(H,x):
    i=H.size
    if i==0:
        H.median=x
    elif i==1:
        if x<=H.median:
            H.Tmin.append(x)
            H.Tmax.append(H.median)
        else:
            H.Tmax.append(x)
            H.Tmin.append(H.median)
        H.median=None            
    else:
        if i%2==0:
            if H.Tmin[0]<=x:
                if H.Tmax[0]>=x:
                    H.median=x
                else:
                    H.median=H.Tmax[0]
                    H.Tmax[0]=x
                    heapify_max(H.Tmax,0,len(H.Tmax))
            else:
                H.median=H.Tmin[0]
                H.Tmin[0]=x
                heapify_min(H.Tmin,0,len(H.Tmin))
        else:
            if H.median<=x:
                H.Tmax.append(x)
                heapify_max_up(H.Tmax,len(H.Tmax)-1)
                H.Tmin.append(H.median)
                heapify_min_up(H.Tmin,len(H.Tmin)-1)
            else:
                H.Tmin.append(x)
                heapify_min_up(H.Tmin,len(H.Tmin)-1)
                H.Tmax.append(H.median)
                heapify_max_up(H.Tmax,len(H.Tmax)-1)
            H.median=None
    H.size+=1
    return

def heapify_max(A,i,n):
    l=2*i+1
    r=2*i+2
    min_ind=i
    if l<n and A[l]<A[min_ind]:
        min_ind=l
    if r<n and A[r]<A[min_ind]:
        min_ind=r
    if min_ind!=i:
        (A[i],A[min_ind])=(A[min_ind],A[i])
        heapify_max(A,min_ind,n)

def heapify_min(A,i,n):
    l=2*i+1
    r=2*i+2
    max_ind=i
    if l<n and A[l]>A[max_ind]:
        max_ind=l
    if r<n and A[r]>A[max_ind]:
        max_ind=r
    if max_ind!=i:
        (A[i],A[max_ind])=(A[max_ind],A[i])
        heapify_min(A,max_ind,n)

def heapify_max_up(A,i):
    p=(i-1)//2
    if p>=0:
        if A[p]>A[i]:
            A[p],A[i]=A[i],A[p]
            heapify_max_up(A,p)

def heapify_min_up(A,i):
    p=(i-1)//2
    if p>=0:
        if A[p]<A[i]:
            A[p],A[i]=A[i],A[p]
            heapify_min_up(A,p)

def extract_median(H):
    if H.median!=None:
        a=H.median
        H.median=None
    else:
        a=(H.Tmax[0]+H.Tmin[0])/2
        H.median=a
        H.Tmax[0],H.Tmax[-1]=H.Tmax[-1],H.Tmax[0]
        H.Tmax.pop()
        heapify_max(H.Tmax,0,len(H.Tmax))
        H.Tmin[0],H.Tmin[-1]=H.Tmin[-1],H.Tmin[0]
        H.Tmin.pop()
        heapify_min(H.Tmin,0,len(H.Tmin))
    H.size-=1
    return a

#testy
H=Heap()
for i in range(20):
    k=randint(1,100)
    insert(H,k)
print(*H.Tmax)
print(*H.Tmin)
print(H.median)
print(extract_median(H))
print(*H.Tmax)
print(*H.Tmin)
print(H.median)
