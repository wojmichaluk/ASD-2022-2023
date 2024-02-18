#Dowolne sortowanie tablicy O(n^2)

from random import randint

#zadanie 1
def bsort(T):
    n=len(T)
    for i in range(n):
        for j in range(1,n-i):
            if T[j-1]>T[j]:
                T[j],T[j-1]=T[j-1],T[j]

#testy
T=[1,63,15,72,8,18,17,65,3,100]
bsort(T)
print(*T)
T=[randint(1,100) for _ in range(25)]
bsort(T)
print(*T)
