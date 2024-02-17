#Wojciech Michaluk
#Algorytm dla każdego pola labiryntu zapisuje
#największą liczbę pól, które można odwiedzić na
#drodze do tego pola (-1 oznacza, że do tego pola
#nie da się dojść). W tym celu w pierwszej kolumnie
#staramy się zajść najdalej jak się da w dół, a każda
#następna kolumna wypełniana jest według zasady:
#jeżeli można wejść na to pole "z lewej" to najpierw
#przepisujemy wartości z poprzedniej, a poźniej
#przechodzimy po kolumnie od góry w dół i od dołu
#do góry, próbując znaleźć "dłuższą" ścieżkę. Szacuję
#złożoność czasową i pamięciową algorytmu na O(n^2).

from zad7testy import runtests

def maze( L ):
    n=len(L)
    D=[[[-1,-1] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if can_move_to(L,i,0):
            D[i][0][1]=i
        else: break
    for j in range(1,n):
        for k in range(n):
            m=max(D[k][j-1])
            if m!=-1 and can_move_to(L,k,j):
                D[k][j]=[m+1,m+1]
        for k in range(1,n):
            if can_move_to(L,k,j) and D[k-1][j][1]!=-1:
                D[k][j][1]=max(D[k][j][1],D[k-1][j][1]+1)
        for k in range(n-2,-1,-1):
            if can_move_to(L,k,j) and D[k+1][j][0]!=-1:
                D[k][j][0]=max(D[k][j][0],D[k+1][j][0]+1)
    return max(D[n-1][n-1])

def can_move_to(L,x,y):
    return L[x][y]!='#'

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
