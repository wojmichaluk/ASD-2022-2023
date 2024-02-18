#A,B - tablice, a,b - liczby naturalne.
#Tablice mają taką samą długość równą n.
#Szukamy najdłuższego wspólnego podciągu 
#w O(n^2). Pomysł: f(i,j) - najdłuższy
#podciąg przy założeniu, że rozważamy
#i elementów z A oraz j elementów z B.
#f(i,j) = max(f(i-1,j), f(i,j-1), f(i-1,j-1) + 1,
#jeśli A[i] == B[j]).

#zadanie 2
def rek_lcs(A,B,i,j):
    if i==0 or j==0: return 0
    if A[i-1]==B[j-1]: return rek_lcs(A,B,i-1,j-1)+1
    return max(rek_lcs(A,B,i-1,j),rek_lcs(A,B,i,j-1))
    
def lcs(A,B): #iteracyjnie, O(n^2)
    n=len(A)
    DP=[[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i==0 or j==0: DP[i][j]=0
            elif A[i-1]==B[j-1]: DP[i][j]=DP[i-1][j-1]+1
            else: DP[i][j]=max(DP[i-1][j],DP[i][j-1])
    return DP[n][n]

#testy
A=[1,3,5,7,9]
B=[1,2,3,4,5]
print(lcs(A,B))
print(rek_lcs(A,B,len(A),len(B)))
A=[1,2,3,4,5,6,7,8,9]
B=[1,2,3,4,5,6,7,8,9]
print(lcs(A,B))
print(rek_lcs(A,B,len(A),len(B)))
A=[1,3,5,7,9,11,13,15]
B=[2,4,6,8,10,12,14,16]
print(lcs(A,B))
print(rek_lcs(A,B,len(A),len(B)))
