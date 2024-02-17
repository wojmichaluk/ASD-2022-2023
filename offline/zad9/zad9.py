#Wojciech Michaluk
#Algorytm najpierw sortuje tablicę parkingów po odległości,
#zachowując spójność z tablicą kosztów. Następnie znajduje
#dla każdej stacji minimalny koszt dojścia w dwóch wariantach:
#dla miasta A koszt to 0, począwszy od tej stacji rozpatrujemy
#koszt dojazdu przy przejechaniu normalnej odległości lub przy
#wykorzystaniu możliwości przejechania dłuższego dystansu,
#przy czym jeżeli wcześniej już tę możliwość wykorzystano, to
#uwzględniany jest tylko pierwszy wariant. W każdym następnym
#kroku zaczynamy od stacji, dla której osiągnięto minimalny koszt
#z poprzedniego kroku. Szacuję złożoność czasową algorytmu na
#O(nlogn), a pamięciową na O(n).

from zad9testy import runtests

def min_cost( O, C, T, L ):
    n=len(O)
    A=[(O[i],C[i]) for i in range(n)]
    A.sort()
    O[0]=C[0]=0
    for i in range(n-1):
        O[i+1]=A[i][0]
        C[i+1]=A[i][1]
    O.append(A[n-1][0])
    O.append(L)
    C.append(A[n-1][1])
    C.append(0)
    DP=[[float('inf') for _ in range(n+2)] for _ in range(2)]
    DP[0][0]=0
    h=k=0
    while h<=n+2:
        i=j=h
        l=k
        min_ind_T1=h+1
        min_ind_T2=k+1
        while i<n+1 and O[i+1]-O[h]<=T:
            DP[0][i+1]=min(DP[0][i+1],DP[0][h]+C[i+1])
            if DP[0][i+1]<=DP[0][min_ind_T1]: min_ind_T1=i+1
            i+=1
        while j<n+1 and O[j+1]-O[h]<=2*T:
            DP[1][j+1]=min(DP[1][j+1],DP[0][h]+C[j+1])
            j+=1
        while l<n+1 and O[l+1]-O[k]<=T:
            DP[1][l+1]=min(DP[1][l+1],DP[1][k]+C[l+1])
            if DP[1][l+1]<=DP[1][min_ind_T2]: min_ind_T2=l+1
            l+=1
        h=min_ind_T1
        k=min_ind_T2
    return DP[1][n+1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
