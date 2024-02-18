#Mamy zbiór punktów X={x1,x2,...,xn} na prostej.
#Szukamy minimalnej liczby przedziałów jednostkowych
#domkniętych, żeby pokryć wszystkie punkty z X.
#Pomysł: sortujemy punkty, jak napotkamy niepokryty
#punkt to zaczynamy przedział.

from random import randint

#zadanie 2
def intervals(A):
    A.sort()
    n=len(A)
    last=0
    res=1
    for i in range(1,n):
        if A[i]>A[last]+1:
            res+=1
            last=i
    return res

#testy
A=[0.5,1.6,0.25]
print(intervals(A))
A=[0.5,4.3,2.14,-6.5,-5.7,1.3,3.04,5.1]
print(intervals(A))
A=[randint(-1000,1000)/100 for _ in range(100)]
#print("randomized:",sorted(A))
print(intervals(A))
