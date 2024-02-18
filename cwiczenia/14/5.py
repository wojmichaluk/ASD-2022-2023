#Dana jest posortowana tablica n liczb,
#chcemy wyznaczyć liczbę x taką, że suma
#różnic bezwględnych |A[i] - x| dla i od 0 do n-1
#jest minimalna. Jaka jest złożoność
#obliczeniowa, czemu algorytm jest poprawny?

#Odpowiedź: Złożoność to O(1). Algorytm jest
#poprawny, bo element o indeksie n//2 jest
#najbliżej środka: dla nieparzystej długości
#to idealnie środkowy element, dla parzystej
#jeden ze środkowych. Bierzemy element możliwie
#środka, bo każde przesunięcie liczby o y powoduje
#wzrost sum dla elementów w kierunku przeciwnym do
#przesunięcia, a spadek dla elementów w kierunku
#zgodnym - dlatego względem elementu środkowego,
#jak się przesuniemy od niego to nowa suma będzie
#nie mniejsza.

from random import uniform

#zadanie 5
def min_abs_sum(A):
    n=len(A)
    if not n: return None
    randoms=[uniform(A[0],A[n-1]) for _ in range(10)]
    randoms[0]=A[n//2]
    sums=[0 for _ in range(10)]
    for i in range(10):
        for j in range(n):
            sums[i]+=abs(A[j]-randoms[i])
    #print(sums)
    #print(randoms)
    return "sum of absolutes: "+str(sums[0]),"number: "+str(randoms[0])

#testy
A=[1,6,7,8,9,10,11]
print(A,min_abs_sum(A),sep='\n')
A=[5,9,11,12,14,19,21,22,25,28]
print(A,min_abs_sum(A),sep='\n')
