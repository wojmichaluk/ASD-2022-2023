#Implementacja domknięcia przechodniego
#grafu (reprezentacja macierzowa)

#zadanie 1
def domkniecie(G):
    n=len(G)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                G[j][k]|=G[j][i]&G[i][k]
    return G

#testy
T,F=True,False
G=[[F,T,F,F],[F,F,T,F],[F,F,F,T],[F,F,F,F]]
print(domkniecie(G),sep='\n')
G=[[F,T,F,F],[T,F,T,F],[F,T,F,T],[F,F,T,F]]
print(domkniecie(G),sep='\n')
G=[[F,T,F,F,F],[F,F,T,F,T],[T,F,F,T,F],[F,F,F,F,F],[F,F,F,F,F]]
print(domkniecie(G),sep='\n')
G=[[F,T,T,F,F],[T,F,T,F,T],[T,T,F,T,F],[F,F,T,F,F],[F,T,F,F,F]]
print(domkniecie(G),sep='\n')
