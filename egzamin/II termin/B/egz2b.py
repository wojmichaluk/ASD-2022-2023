#Wojciech Michaluk
#Algorytm znajduje najmniejsze sumy
#odległości parkingów od biurowców,
#rozważając (jeżeli to możliwe) sumę odległości
#dla danego parkingu i biurowca, zakładając, że
#danemu biurowcowi będzie odpowiadał tenże
#parking. Wyniki zapisuje w tabeli i wybiera
#wartość najmniejszą dla ostatniego parkingu.
#Dla konfiguracji niemożliwych (np. nie każdy
#biurowiec miałby parking) umownie przyjmuję
#odległość nieskończoność. Szacuję złożoność
#czasową jak i pamięciową algorytmu na O(mn).

from egz2btesty import runtests

#O(mn)
def parking(X,Y):
    n=len(X)
    m=len(Y)
    DP=[[float('inf') for _ in range(m)] for _ in range(n)]
    DP[0][0]=abs(X[0]-Y[0])
    for i in range(1,n):
        DP[i][i]=abs(X[i]-Y[i])+DP[i-1][i-1]
    for i in range(1,m-n+1):
        DP[0][i]=abs(X[0]-Y[i])
    for i in range(1,n):
        mini=float('inf')
        if m>n: mini=min(DP[i-1][i-1],DP[i-1][i])
        for j in range(i+1,m-n+i+1):
            DP[i][j]=abs(X[i]-Y[j])+mini
            mini=min(mini,DP[i-1][j])
    return min(DP[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
