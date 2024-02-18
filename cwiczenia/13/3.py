#A[n] - długości samochodów, które stoją
#w kolejce do promu. Prom ma dwa pasy (lewy
#i prawy każdy długości l). Należy wyznaczyć,
#które samochody powinny pojechać na który pas,
#żeby na promie zmieściło się najwięcej aut.
#Auta wjeżdżają w takiej kolejności, jak w tablicy A.
#Pomysł: f(i,l1,l2) = max(f(i-1,l1-c_i,l2) [gdy l1>=c_i],
#f(i-1,l1,l2-c_i) [gdy l2>=c_i]) + 1, 0 w przeciwnym 
#przypadku. Wynik: max(f(i,l,l) == i) dla i=0,1,...,n-1. 

from random import randint

#zadanie 3
def cars(i,l1,l2,c): #rekurencja
    if i==0: return 0
    maks=0
    if l1>=c[i-1]:
        maks=cars(i-1,l1-c[i-1],l2,c)+1
    if l2>=c[i-1]:
        maks=max(maks,cars(i-1,l1,l2-c[i-1],c)+1)
    return maks

def cars2(l1,l2,c): #dynamik
    n=len(c)
    DP=[[[0 for _ in range(l2+1)] for _ in range(l1+1)] for _ in range(n+1)]
    for i in range(l1+1):
        DP[0][i][l2]=1
    for i in range(l2+1):
        DP[0][l1][i]=1
    i=1
    while i<n+1:
        prog=0
        for j in range(l1+1):
            for k in range(l2+1):
                if DP[i-1][j][k]:
                    if j>=c[i-1]:
                        DP[i][j-c[i-1]][k]=1
                        prog=1
                    if k>=c[i-1]:
                        DP[i][j][k-c[i-1]]=1
                        prog=1
        if not prog: break
        i+=1
    return i-1

#testy
c=[3,5,5,5]
print(cars(len(c),9,9,list(reversed(c))))
print(cars2(9,9,c))
print()
c=[7,11,6,2,5,9,4,7,8]
print(cars(len(c),27,27,list(reversed(c))))
print(cars2(27,27,c))
for i in range(10):
    print()
    c=[randint(3,12) for _ in range(25)]
    print(cars(len(c),80,80,list(reversed(c))))
    print(cars2(80,80,c))
