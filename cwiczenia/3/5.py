#Struktura danych z operacjami insert, extract_min, extract_max.
#Operacje mają być w złożoności O(logn). Pomysł: mamy dwa kopce -
#min i max, dla każdego elementu w danym kopcu zapamiętujemy
#pozycję w drugim kopcu.

#nie działa :(

from random import randint

#zadanie 5
class Heap:
    def __init__(self):
        self.Tmax=[]
        self.Tmin=[]

def insert(H,x):
    l=len(H.Tmax)
    H.Tmax.append((x,))
    H.Tmin.append((x,))
    max_ind=heapify_max_up(H.Tmax,l,H.Tmin)
    min_ind=heapify_min_up(H.Tmin,l,H.Tmax)
    H.Tmax[max_ind]+=(min_ind,)
    H.Tmin[min_ind]+=(max_ind,)

def heapify_min(A,i,n,B):
    l=2*i+1
    r=2*i+2
    min_ind=i
    if l<n and A[l][0]<A[min_ind][0]:
        min_ind=l
    if r<n and A[r][0]<A[min_ind][0]:
        min_ind=r
    if min_ind!=i:
        B[A[i][1]]=(B[A[i][1]][0],min_ind)
        B[A[min_ind][1]]=(B[A[min_ind][1]][0],i)
        (A[i],A[min_ind])=(A[min_ind],A[i])
        heapify_min(A,min_ind,n,B)

def heapify_max(A,i,n,B):
    l=2*i+1
    r=2*i+2
    max_ind=i
    if l<n and A[l][0]>A[max_ind][0]:
        max_ind=l
    if r<n and A[r][0]>A[max_ind][0]:
        max_ind=r
    if max_ind!=i:
        B[A[i][1]]=(B[A[i][1]][0],max_ind)
        B[A[max_ind][1]]=(B[A[max_ind][1]][0],i)
        (A[i],A[max_ind])=(A[max_ind],A[i])
        heapify_max(A,max_ind,n,B)

def heapify_min_up(A,i,B):
    p=(i-1)//2
    if p>=0:
        if A[p][0]>A[i][0]:
            B[A[p][1]]=(B[A[p][1]][0],i)
            A[p],A[i]=A[i],A[p]    
            return heapify_min_up(A,p,B)
    return i

def heapify_max_up(A,i,B):
    p=(i-1)//2
    if p>=0:
        if A[p][0]<A[i][0]:
            B[A[p][1]]=(B[A[p][1]][0],i)
            A[p],A[i]=A[i],A[p]
            return heapify_max_up(A,p,B)
    return i

def extract_max(H):
    a=H.Tmax[0]
    i=a[1]
    l=len(H.Tmax)
    """if i==l-1:
        print("no")
        if H.Tmax[1]>H.Tmax[2]:
            H.Tmin[i]=(H.Tmax[1][0],H.Tmin[i][1])
            i=H.Tmax[1][1]
        else:
            H.Tmin[i]=(H.Tmax[2][0],H.Tmin[i][1])
            i=H.Tmax[2][1]"""
    H.Tmax[0],H.Tmax[l-1]=H.Tmax[l-1],H.Tmax[0]
    H.Tmin[H.Tmax[0][1]]=(H.Tmin[H.Tmax[0][1]][0],0)
    H.Tmax.pop()
    heapify_max(H.Tmax,0,l-1,H.Tmin)
    print("i:",i)
    H.Tmin[i],H.Tmin[l-1]=H.Tmin[l-1],H.Tmin[i]
    H.Tmax[H.Tmin[i][1]]=(H.Tmax[H.Tmin[i][1]][0],i)
    H.Tmin.pop()
    heapify_min(H.Tmin,i,l-1,H.Tmax)
    return a[0]

def extract_min(H):
    a=H.Tmin[0]
    i=a[1]
    l=len(H.Tmin)
    """if i==l-1:
        print("no")
        if H.Tmin[1]<H.Tmin[2]:
            H.Tmax[i]=(H.Tmin[1][0],H.Tmin[i][1])
            i=H.Tmin[1][1]
        else:
            H.Tmax[i]=(H.Tmax[2][0],H.Tmin[i][1])
            i=H.Tmin[2][1]"""
    H.Tmin[0],H.Tmin[l-1]=H.Tmin[l-1],H.Tmin[0]
    H.Tmax[H.Tmin[0][1]]=(H.Tmax[H.Tmin[0][1]][0],0)
    H.Tmin.pop()
    heapify_min(H.Tmin,0,l-1,H.Tmax)
    print("i:",i)
    H.Tmax[i],H.Tmax[l-1]=H.Tmax[l-1],H.Tmax[i]
    H.Tmin[H.Tmax[i][1]]=(H.Tmin[H.Tmax[i][1]][0],i)
    H.Tmax.pop()
    heapify_max(H.Tmax,i,l-1,H.Tmin)
    return a[0]

#testy
H=Heap()
for i in range(20):
    k=randint(1,100)
    insert(H,k)
for i in range(20):
    print(H.Tmax[i][0],end=' ')
print()
for i in range(20):
    print(H.Tmin[i][0],end=' ')
print()
print(extract_max(H))
for i in range(19):
    print(H.Tmax[i][0],end=' ')
print()
for i in range(19):
    print(H.Tmin[i][0],end=' ')
print()
print(extract_min(H))
for i in range(18):
    print(H.Tmax[i][0],end=' ')
print()
for i in range(18):
    print(H.Tmin[i][0],end=' ')
print()
print(*sorted(H.Tmax))
print(*sorted(H.Tmin))
