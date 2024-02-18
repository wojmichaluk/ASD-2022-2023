#Las rosnący na osi liczbowej (pozycje
#od 0 do n-1, n drzew). Dla każdego i znamy
#zysk c_i. Chcemy uzyskać maksymalny zysk,
#ale nie można ścinać dwóch drzew z rzędu.
#Pomysł: f(i) = max(c_i + f(i-2), f(i-1))
#dla i>=2; c_0 dla i==0; max(c_0, c_1) dla i==1.
#f(n-1) - szukany wynik.

from random import randint

#zadanie 1
def las1(i,c): #rekurencyjnie
    if i==0: return c[0]
    if i==1: return max(c[0],c[1])
    return max(c[i]+las1(i-2,c),las1(i-1,c))

def forest(i,c,values): #rekurencja ze spamiętywaniem
    if i==0: return c[0]
    if i==1: return max(c[0],c[1])
    if values[i]==None:
        values[i]=max(c[i]+forest(i-2,c,values),forest(i-1,c,values))
    return values[i]

def las2(c):
    n=len(c)
    values=[None for _ in range(n)]
    return forest(n-1,c,values)

def las3(c): #iteracyjnie
    n=len(c)
    values=[0 for _ in range(n)]
    values[0]=c[0]
    values[1]=max(c[0],c[1])
    for i in range(2,n):
        values[i]=max(c[i]+values[i-2],values[i-1])
    return values[n-1]

#testy
c=[2,3,5,7]
print(las1(len(c)-1,c))
print(las2(c))
print(las3(c))
print()
c=[4,2,6,1,3,2,7,9]
print(las1(len(c)-1,c))
print(las2(c))
print(las3(c))
print()
c=[randint(5,15) for _ in range(30)]
print(las1(len(c)-1,c))
print(las2(c))
print(las3(c))
