#Znaleźć uniwersalne ujście t: 1) dla każdego
#wierzchołka v istnieje krawędź z v do t oraz
#2) t nie posiada krawędzi wychodzących. Dane są
#G - graf skierowany jako macierz sąsiedztwa. Pomysły:
#Bruteforce (O(n^2)) - szukamy wiersza, w którym są
#same zera i jednocześnie kolumnę z n-1 jedynkami - 
#przecięcie to szukany wierzchołek. Rozwiązanie O(n):
#ustawiamy się w lewym górnym rogu, jeżeli 0 to idziemy
#w prawo, jeżeli 1 to w dół, powtarzamy aż do prawej 
#krawędzi - mamy potencjalnego kandydata.

#zadanie 4
def bruteforce(G):
    n=len(G)
    for i in range(n):
        a=True
        for j in range(n):
            if G[i][j]!=0:
                a=False
                break
        if not a: continue
        for j in range(n):
            if j==i: continue
            if G[j][i]!=1:
                a=False
                break
        if a: return (True,i)
    return (False,None)

def find_outlet(G):
    i=j=0
    n=len(G)
    while i<n and j<n:
        if G[i][j]==0: j+=1
        else: i+=1
    for k in range(n):
        if G[i][k]==1: return (False,None)
    for k in range(n):
        if k==i: continue
        if G[k][i]==0: return (False,None)
    return (True,i)

#testy
G=[[0,0,0,0,1],[1,0,0,0,1],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0]]
print(bruteforce(G))
print(find_outlet(G))
G=[[0,0,0,1,1,0,0],[1,0,0,0,1,0,0],[0,0,0,0,1,0,0],
[0,0,0,0,1,0,0],[0,0,0,0,0,0,1],[1,0,1,1,1,0,0],[1,0,0,0,0,1,0]]
print(bruteforce(G))
print(find_outlet(G))
G=[[0,1,0,0,1,1],[0,0,1,0,1,0],[0,0,0,0,1,0],
[0,0,1,0,1,0],[0,0,0,0,0,0],[0,0,0,0,1,0]]
print(bruteforce(G))
print(find_outlet(G))
