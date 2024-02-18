#Oazy i miasta - w miastach są drzwi północne
#i południowe, z każdymi drzwiami jest połączona
#oaza lub inne miasto, oazy mogą łączyć się dowolnie.
#Chcemy odwiedzić każde miasto dokładnie raz. Pomysł:
#1) Oazy połączone scalamy w jeden wierzchołek.
#2) Miasta zamieniamy na krawędzie. 3) Euler

#zadanie 6
def CitiesAndOasis(G):
    def DFSVisit(G,u):
        nonlocal visited
        visited[u]=True
        if G[u][0]=='O':
            for v in G[u][1]:
                if not visited[v]:
                    DFSVisit(G,v)
        else:
            nonlocal cities
            cities.append(u)
    n=len(G)
    visited=[False for _ in range(n)]
    cities=[]
    Gr=[]
    for i in range(n):
        if G[i][0]=='O' and not visited[i]:
            DFSVisit(G,i)
            for i in range(len(cities)):
                visited[cities[i]]=False
            Gr.append(cities)
            cities=[]
    edges=[[] for _ in range(len(Gr))]
    for i in range(len(Gr)):
        for j in range(len(Gr[i])):
            city=Gr[i][j]
            for k in range(len(Gr)):
                if (k!=i and city in Gr[k]) or found(Gr[k],G[city][1]):
                    edges[i].append(k)
                    break
    return HasEulerCycle(edges)

def found(tab1,tab2):
    n=len(tab1)
    for i in range(n):
        if tab1[i] in tab2: return True
    return False

def HasEulerCycle(G):
    n=len(G)
    for i in range(n):
        if len(G[i])%2!=0: return False
    return True

#testy
G=[('C',[1,2]),('C',[0,4]),('O',[0,3]),('O',[2,4,5]),('O',[1,3,6,8]),
('C',[3,6]),('O',[4,5,7]),('C',[6,8]),('O',[4,7]),('O',[])]
print(CitiesAndOasis(G))
G=[('O',[1,2]),('O',[0,2,3]),('O',[0,1,3,4]),('O',[1,2,13]),('C',[2,5]),
('O',[4,6]),('O',[5,7]),('O',[6,8]),('C',[7,9]),('O',[8,10,12]),('O',[9,11,12]),
('O',[10,12,13]),('O',[9,10,11]),('C',[3,11])]
print(CitiesAndOasis(G))
G=[('O',[1,2]),('O',[0,2,3]),('O',[0,1,3,4]),('O',[1,2,4,13]),('C',[2,3]),
('O',[6]),('O',[5,7]),('O',[6,8]),('C',[7,9]),('O',[8,10,12]),('O',[9,11,12]),
('O',[10,12,13]),('O',[9,10,11]),('C',[3,11])]
print(CitiesAndOasis(G))
G=[('O',[1,2]),('O',[0,2,3]),('O',[0,1,3,4]),('O',[1,2,15]),('C',[2,14]),
('O',[14,6]),('O',[5,7]),('O',[6,8]),('C',[7,9]),('O',[8,10,12]),('O',[9,11,12]),
('O',[10,12,13]),('O',[9,10,11]),('C',[11,15]),('C',[4,5]),('C',[3,13])]
print(CitiesAndOasis(G))
