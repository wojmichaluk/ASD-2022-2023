#A - tablica, zawiera liczby naturalne. Szukamy
#B - podzbioru A, tak żeby suma po elementach B
#wynosiła T (zadana liczba naturalna). Pomysły do
#dynamików: 1) tworzymy tablicę o długości T+1, na 
#pierwszej pozycji True, na pozostałych False
#(indeks = wartość, True kiedy można osiągnąć,
#False jeżeli nie). Idziemy od końca po wartościach
#z A, jeżeli na indeksie i - A[j] jest True, to na
#indeksie i ustawiamy True. 2) f(i,v) = True, jeżeli
#v==0 lub f(i+1,v) == True lub f(i+1,v-A[i]) == True,
#False w przeciwnym przypadku.

from random import randint

#zadanie 1
def rek_sumT(A,v,i=0): #rekurencyjnie
    if v==0: return True
    if v<0 or i==len(A): return False
    return rek_sumT(A,v,i+1) or rek_sumT(A,v-A[i],i+1)
    
def sumT(A,T): #dynamik v1
    tab=[False for _ in range(T+1)]
    tab[0]=True
    n=len(A)
    for i in range(n-1,-1,-1):
        for j in range(T,A[i]-1,-1):
            if tab[j-A[i]]: tab[j]=True
    return tab[T]

def sumT2(A,T): #dynamik v2
    n=len(A)
    m=T
    DP=[[False for _ in range(m+1)] for _ in range(n)]
    for i in range(n):
        DP[i][0]=True
    if A[0]<=T: DP[0][A[0]]=True
    for i in range(1,n):
        for j in range(m+1):
            if DP[i-1][j]: DP[i][j]=True
        for j in range(A[i],m+1):
            if DP[i-1][j-A[i]]: DP[i][j]=True
    return DP[n-1][T]

#testy
A=[2,3,5]
print(sumT(A,7))
print(sumT(A,4))
print(sumT2(A,7))
print(sumT2(A,4))
print(rek_sumT(A,7))
print(rek_sumT(A,4))
A=[randint(1,1000) for _ in range(50)]
print(sumT(A,50729))
print(sumT(A,413))
print(sumT2(A,50729))
print(sumT2(A,413))
#print(rek_sumT(A,50729))
#print(rek_sumT(A,413))
