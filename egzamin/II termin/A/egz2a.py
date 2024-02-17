#Wojciech Michaluk
#Najpierw tworzona jest tablica T, taka że T[i] oznacza
#liczbę punktów o y>=i, następnie tablica DP, w której
#dla każdej współrzędnej x-owej obliczana jest liczba
#punktów o tej współrzędnej i największa współrzędna
#y-owa wśród nich. Algorytm, bazując na tych tablicach
#znajduje dla każdego x-a(biorę punkt z największym y,
#bo on będzie dominował nie mniej niż pozostałe) jego
#siłę według wzoru: siła=n-T[DP[i][1]]-j-DP[i][0]+1, gdzie
#j-liczba punktów o współrzędnej x-owej większej, DP[i]=
#(liczba punktów o x=i,największy y dla tych punktów);
#zwracana jest największą znaleziona wartość. Szacuję
#złożoność czasową i pamięciową algorytmu na O(n).

from egz2atesty import runtests

#O(n), na podstawie kodu by Błażej Dudek
def dominance(P):
    n=len(P)
    T=[0 for _ in range(n+1)]
    for i in range(n):
        T[P[i][1]]+=1
    for i in range(n-1,-1,-1):
        T[i]+=T[i+1]
    DP=[(0,0) for _ in range(n+1)]
    for i in range(n):
        x,y=P[i]
        curr=DP[x][0]+1
        maxi=max(DP[x][1],y)
        DP[x]=(curr,maxi)
    max_dom=0
    j=0
    for i in range(n,0,-1):
        a=n-T[DP[i][1]]-j-DP[i][0]+1
        j+=DP[i][0]
        max_dom=max(max_dom,a)
    return max_dom

"""
#Wojciech Michaluk
#Algorytm dla każdego punktu oblicza
#jego siłę, porównując go z każdym z
#pozostałych punktów i sprawdzając,
#czy go dominuje. Nastepnie zwraca
#największą znalezioną wartość (czyli
#siłę najsilniejszego z nich). Szacuję
#złożoność czasową na O(n^2), a
#pamięciową na O(n).

#O(n^2)
def dominance(P):
    n=len(P)
    D=[0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dominating(P[i],P[j]):
                D[i]+=1
    return max(D)

def dominating(P1,P2):
    return P1[0]>P2[0] and P1[1]>P2[1]
"""

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True)
