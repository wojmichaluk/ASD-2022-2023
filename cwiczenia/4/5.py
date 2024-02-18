#Mamy tablicę A rozmiaru n, A[i] ma wartości ze
#zbioru {0,1,...,k-1}. Chcemy znaleźć najmniejszy
#podprzedział A, który zawiera wszystkie kolory 
#(wartości). Pomysł: zaczynamy od początku tablicy,
#rozszerzamy przedział aż znajdziemy wszystkie kolory.
#Wtedy przesuwamy początkowy wskaźnik, dopóki będziemy
#mieć wszystkie kolory - jeżeli nie, to przesuwamy
#wskaźnik końca.

#zadanie 5
def shortest_containing_all(A,k):
    n=len(A)
    if k>n: return False
    i=j=0
    T=[]
    while j<n:
        a=binary_search(T,A[j],0,len(T)-1)
        if a[0]: T[a[1]]=(T[a[1]][0],T[a[1]][1]+1)
        else: T=T[:a[1]]+[(A[j],1)]+T[a[1]:]
        if len(T)==k: break
        j+=1
    if j==n: return False
    a=(0,j)
    if j-i==k-1: return a
    while j<n:
        i+=1
        if T[A[i-1]][1]==1:
            while j<n and A[j]!=A[i-1]:
                T[A[j]]=(T[A[j]][0],T[A[j]][1]+1)
                j+=1
            if j==n: return a
            if j-i<a[1]-a[0]: a=(i,j)
        else:
            T[A[i-1]]=(T[A[i-1]][0],T[A[i-1]][1]-1)
            a=(i,j)
            if j-i==k-1: return a
    return a   

def binary_search(A,el,p,r):
    mid=(p+r)//2
    if p>r: return (False,mid+1)
    if A[mid][0]==el: return (True,mid)
    if A[mid][0]>el: return binary_search(A,el,p,mid-1)
    return binary_search(A,el,mid+1,r)

#testy
T=[0,2,1,0,2,2,0,2,3,3,2,1,0,3]
print(shortest_containing_all(T,4))
