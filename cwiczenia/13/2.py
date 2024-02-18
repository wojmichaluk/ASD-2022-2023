#Każdy klocek to przedział <a;b>. Dany jest
#ciąg n klocków, klocki spadają w takiej
#kolejności, w jakiej są w ciągu. Szukamy min.
#klocków do usunięcia, żeby każdy kolejny klocek
#mieścił się w całości w tym, który spadł tuż
#przed nim. Pomysł: g(j) to klocek na szczycie
#wieży {0,1,...,j}, f(i) = min(f(i-1) + 1, i, 
#min(f(j) + (i-j+1) | (ai, bi) <= g(j) dla j<i));
#f(0) = 0.

from random import randint

#zadanie 2
def blocks(A): #rekurencja ze spamiętywaniem
    n=len(A)
    tab=[-1 for _ in range(n)]
    top=[None for _ in range(n)]
    return block_tower(A,tab,top,n-1)

def block_tower(A,tab,top,i):
    if i==0:
        top[i]=A[i]
        tab[0]=0
        return 0
    if tab[i]==-1:
        min_take=float('inf')
        b=float('inf')
        for j in range(i):
            b=block_tower(A,tab,top,j)+(i-j-1)
            if upper(A[i],top[j]) and b<min_take:
                min_take=b
        tab[i]=min(block_tower(A,tab,top,i-1)+1,min_take,i)
        if tab[i]==block_tower(A,tab,top,i-1)+1: top[i]=top[i-1]
        else: top[i]=A[i]
    return tab[i]

def upper(el,t):
    return el[0]>=t[0] and el[1]<=t[1]

def dynamic(A): #dynamik
    n=len(A)
    tab=[-1 for _ in range(n)]
    top=[None for _ in range(n)]
    tab[0]=0
    top[0]=A[0]
    for i in range(1,n):
        min_take=float('inf')
        b=float('inf')
        for j in range(i):
            if upper(A[i],top[j]):
                b=tab[j]+(i-j-1)
                if b<min_take:
                    min_take=b
        tab[i]=min(tab[i-1]+1,min_take,i)
        if tab[i]==tab[i-1]+1: top[i]=top[i-1]
        else: top[i]=A[i]
    return tab[n-1]

#testy
A=[(1,6),(2,8),(2.5,5),(9,12),(3.5,4.5)]
print(blocks(A))
print(dynamic(A))
A=[(1,12),(2,11),(3,10),(4,9),(5,8),(6,7)]
print(blocks(A))
print(dynamic(A))
A=[(randint(1+2*i,100),randint(101,200-2*i)) for i in range(50)]
print(blocks(A))
print(dynamic(A))
