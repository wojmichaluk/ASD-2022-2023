#Dany jest graf G jako macierz sąsiedztwa.
#Czy istnieje cykl długości 4? Bruteforce
#(O(n^4)): sprawdzamy każdą możliwą czwórkę
#wierzchołków; O(n^3): 1) Rozważamy pary
#wierzchołków, dla danej pary sprawdzamy, czy
#istnieją jakieś wierzchołki x, y, tak, aby
#były one z nimi połączone.

#zadanie 3
def cykl4_brute(G):
    n=len(G)
    for i in range(n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    if G[i][j] and G[i][k] and G[j][l] and G[k][l]: return True
                    elif G[i][j] and G[i][l] and G[j][k] and G[l][k]: return True
                    elif G[i][k] and G[i][l] and G[k][j] and G[l][j]: return True
    return False

def cykl4(G):
    n=len(G)
    for i in range(n-1):
        for j in range(i+1,n):
            c=0
            for k in range(n):
                if G[i][k] and G[j][k]: c+=1
            if c>=2: return True
    return False

#testy
G=[[0,0,0,1,1,0],[0,0,0,1,0,1],[0,0,0,1,0,1],
[1,1,1,0,0,0],[1,0,0,0,0,0],[0,1,1,0,0,0]]
print(cykl4_brute(G))
print(cykl4(G))
G=[[0,0,1,1,1],[0,0,1,1,0],[1,1,0,0,1],[1,1,0,0,1],[1,0,1,1,0]]
print(cykl4_brute(G))
print(cykl4(G))
G=[[0,1,1,1,0,0],[1,0,1,0,0,0],[1,1,0,0,0,0],
[1,0,0,0,1,1],[0,0,0,1,0,1],[0,0,0,1,1,0]]
print(cykl4_brute(G))
print(cykl4(G))
