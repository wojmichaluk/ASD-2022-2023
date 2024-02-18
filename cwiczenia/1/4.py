#T - posortowana tablica liczb, x - liczba dodatnia.
#Sprawdź, czy istnieją indeksy i,j takie, że T[j]-T[i]==x

from random import randint

#zadanie 4
def indexes(T,x):
    i=0
    j=1
    while j<len(T):
        diff=T[j]-T[i]
        if diff==x:
            return True,i,j
        if diff<x:
            j+=1
        else:
            i+=1
    return False

#testy
T=[1,3,8,15,17,18,63,65,72,100]
print(*T)
print(indexes(T,9))
print(indexes(T,18))
T=[randint(1,100) for _ in range(25)]
T.sort()
print(*T)
print(indexes(T,9))
print(indexes(T,18))
