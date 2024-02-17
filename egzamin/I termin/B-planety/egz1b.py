#Wojciech Michaluk
#Algorytm dla każdej planety wyznacza
#minimalny koszt dostania się na nią, mając
#daną ilość paliwa w baku, przy czym dla A
#jest to koszt 0 dla pustego baku. Następnie
#rozważa koszty dostania się z tej planety na
#następną planetę (nie trzeba rozpatrywać
#wszystkich planet "w zasięgu" dzięki pamiętaniu
#ilości paliwa), uwzględnia także opcję teleportu
#(jeżeli to możliwe). Szacuję złożoność czasową
#algorytmu na O(nE), pamięciową też na O(nE).

from egz1btesty import runtests

def planets( D, C, T, E ):
    n=len(D)
    costs=[[float('inf') for _ in range(E+1)] for _ in range(n)]
    costs[0][0]=0
    for i in range(n-1):
        for j in range(1,E+1):
            costs[i][j]=min(costs[i][j],costs[i][j-1]+C[i])
        if T[i][0]>i: costs[T[i][0]][0]=min(costs[T[i][0]][0],costs[i][0]+T[i][1])
        dist=D[i+1]-D[i]
        for k in range(dist,E+1):
            costs[i+1][k-dist]=min(costs[i+1][k-dist],costs[i][k])
    return costs[n-1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
