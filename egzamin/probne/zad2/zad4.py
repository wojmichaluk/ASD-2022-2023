#Wojciech Michaluk
#Algorytm najpierw sortuje budynki względem końców
#podstaw, zapamiętując oryginalny indeks i dodaje na
#końcu sztuczny budynek (na potrzeby rekurencji).
#Następnie dla każdego budynku w tej tablicy wyznacza
#dynamicznie największą możliwą pojemność, jaką można
#uzyskać do tego budynku włącznie, rozpatrując przypadki,
#w których bierzemy dany budynek (jeżeli nie zostanie
#przekroczony budżet i budynki nie będą się pokrywać) oraz
#wariant, w którym go nie bierzemy. Końcowo, odczytując
#wstecz, zwracana jest lista budynków dla największej
#znalezionej pojemności. Szacuję złożoność czasową
#algorytmu na O(n^2), a pamięciową na O(pn).

from zad4testy import runtests

#wersja O(n^2), na podstawie kodu by Jakub Karczewski
def select_buildings(T,p):
    n=len(T)
    DP=[[-1 for _ in range(p+1)] for _ in range(n+1)]
    par=[[[-1,-1] for _ in range(p+1)] for _ in range(n+1)]
    M=[(T[i][2],T[i][1],T[i][0],T[i][3],i) for i in range(n)]
    M.sort()
    max_b=M[n-1][0]
    M.append((max_b+1, max_b+1,0,0,n))
    res=solve(M,DP,par,n,0,p)
    x,x_p=par[n][0]
    tab=[]
    while x!=-1:
        tab.append(M[x][4])
        x,x_p=par[x][x_p]
    tab.reverse()
    return tab

def solve(M,DP,par,i,price,p):
    if DP[i][price]!=-1:
        return DP[i][price]
    b,a,h=M[i][0],M[i][1],M[i][2]
    maxi=h*(b-a)
    for j in range(i-1,-1,-1):
        b2,a2,c2=M[j][0],M[j][1],M[j][3]
        if b2<a and price+c2<=p:
            curr=h*(b-a)+solve(M,DP,par,j,price+c2,p)
            if curr>maxi:
                par[i][price]=j,price+c2
                maxi=curr
    DP[i][price]=maxi
    return maxi

"""
#Wojciech Michaluk
#Algorytm najpierw sortuje budynki względem końców
#podstaw, zapamiętując oryginalny indeks. Następnie dla
#każdego budynku w tej tablicy oraz dla każdego kosztu
#od 0 do p włącznie wyznacza dynamicznie największą
#możliwą pojemność, jaką można uzyskać do tego budynku
#włącznie, rozpatrując przypadki, w których bierzemy dany
#budynek (jeżeli nie zostanie przekroczony budżet i budynki
#nie będą się pokrywać) oraz wariant, w którym go nie
#bierzemy. Końcowo, odczytując wstecz, zwracana jest
#lista budynków dla największej znalezionej pojemności.
#Szacuję złożoność czasową algorytmu na O(pn^2), a
#pamięciową na O(pn).

#wersja O(n^2p), na podstawie kodu by Jasiek Kalęba
def collide(T,i,j):
    return not (T[i][2]<T[j][1] or T[i][1]>T[j][2])

def select_buildings(T,p):
    n=len(T)    
    F=[[0 for _ in range(p+1)] for _ in range(n)]
    T2=[(T[i][0],T[i][1],T[i][2],T[i][3],i) for i in range(n)]
    T2.sort(key=lambda x: x[2])
    T.sort(key=lambda x: x[2])
    indices=[el[4] for el in T2]
    capacities=[T[i][0]*(T[i][2]-T[i][1]) for i in range(n)]
    for c in range(T[0][3],p+1):
        F[0][c]=capacities[0]
    for i in range(1,n):
        for c in range(p+1):
            F[i][c]=F[i-1][c]
            if c>=T[i][3]:
                for j in range(i-1,-1,-1):
                    if not collide(T,i,j):
                        F[i][c]=max(F[i][c],F[j][c-T[i][3]]+capacities[i])
                        break
                    else:
                        F[i][c]=max(F[i][c],capacities[i])
    i=n-1
    c=p
    result=[]
    while i>=0:
        if i>0 and F[i][c]!=F[i-1][c]:
            after=F[i][c]
            result.append(indices[i])
            curr=capacities[i]
            c-=T[i][3]
            j=i-1
            while j>=0 and F[j][c]+curr!=after:
                j-=1
                i-=1
        elif i==0 and F[i][c]!=0:
            result.append(indices[i])
        i-=1
    return sorted(result)
"""

runtests( select_buildings )
