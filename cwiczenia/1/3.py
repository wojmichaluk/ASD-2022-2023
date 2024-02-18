#Algorytm znajdujący jednocześnie minimum i maksimum,
#używając około (3/2)*n porównań (n - rozmiar tablicy)

from random import randint

#zadanie 3
def min_max(T):
    n=len(T)
    gus=zus=T[-1]
    for i in range(1,n,2):
        if T[i]<T[i-1]:
            mi,ma=T[i],T[i-1]
        else:
            mi,ma=T[i-1],T[i]
        gus=max(gus,ma)
        zus=min(zus,mi)
    return zus,gus

#testy
T=[63,15,72,1,8,18,17,100,65,3]
print(*T)
print(min_max(T))
T=[randint(1,100) for _ in range(25)]
print(*T)
print(min_max(T))
