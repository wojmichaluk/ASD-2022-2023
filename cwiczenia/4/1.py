#Dana jest tablica n liczb ze zbioru {0,1,...,n^2-1}.
#Chcemy ją posortować. Pomysł: najpierw sortowanie po
#modulo n, później div n (dzielenie całkowite).

from random import randint

#zadanie 1
def radix_sort(T):
    n=len(T)
    T=counting_sort(T,n,1)
    T=counting_sort(T,n,2)
    return T

def counting_sort(T,k,t):
    n=len(T)
    output=[0]*n
    count=[0]*k
    if t==1:
        for i in range(n):
            count[T[i]%k]+=1
        for i in range(1,k):
            count[i]+=count[i-1]
        for i in range(n-1,-1,-1):
            output[count[T[i]%k]-1]=T[i]
            count[T[i]%k]-=1
    elif t==2:
        for i in range(n):
            count[T[i]//k]+=1
        for i in range(1,k):
            count[i]+=count[i-1]
        for i in range(n-1,-1,-1):
            output[count[T[i]//k]-1]=T[i]
            count[T[i]//k]-=1
    return output

#testy
n=1000000
T=[randint(0,n*n-1) for _ in range(n)]
T[n//3]=0
T[(2*n)//3]=n*n-1
T=radix_sort(T)
print(*T[:20])
print(*T[n-20:])
