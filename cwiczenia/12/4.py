#A1,A2,...,An - ciąg macierzy. Chcemy je
#wymnożyć, znamy rozmiary macierzy. Szukamy
#takiej kolejności, żeby koszt (liczba operacji)
#był jak najmniejszy.

#UWAGA - program raczej zwraca ilość tych
#operacji, a nie samą kolejność. Uzupełnienie tego
#feature'a pozostawiam jako ćwiczenie dla czytelnika :D.

#zadanie 4
def lowest_cost(D):
    n=len(D)
    DP=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(1,n):
        for j in range(i,n):
            DP[j-i][j]=min(DP[j-i+1][j]+D[j-i][0]*D[j-i][1]*D[j][1],DP[j-i][j-1]+D[j-i][0]*D[j][0]*D[j][1])
    return DP[0][n-1]

#testy
Dims=[(2,3),(3,2),(2,4),(4,5),(5,3)]
print(lowest_cost(Dims))
Dims=[(4,10),(10,19),(19,17),(17,1),(1,15),(15,12),(12,4)]
print(lowest_cost(Dims))
Dims=[(1,1),(1,1),(1,1)]
print(lowest_cost(Dims))
