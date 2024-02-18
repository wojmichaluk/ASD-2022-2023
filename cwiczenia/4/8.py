#"Przesuwanie" początkowych k elementów na koniec.

from random import randint

#zadanie 8
def MovedByK(T,k):
    T[:k]=T[:k][::-1]
    T[k:]=T[k:][::-1]
    T=T[::-1]
    return T

#testy
T=[randint(1,1000) for _ in range(50)]
T.sort()
k=randint(15,25)
print(*T)
T=MovedByK(T,k)
print(*T)
