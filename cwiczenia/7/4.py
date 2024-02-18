#Sprawdzenie, czy w danym grafie jest
#cykl Eulera. Jeżeli tak, to podajemy go.

#zadanie 4
def EulerCycle(G,start_v):
    def DFSVisit(G,u):
        nonlocal cycle
        for i in range (len(G[u])):
            if G[u][i]:
                G[u][i]=0
                G[i][u]=0
                DFSVisit(G,i)
        cycle.append(u)
    n=len(G)
    for i in range(n):
        if len(G[i])==0 or len(G[i])%2!=0: return False
    M=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            M[i][j]=1
    cycle=[]
    DFSVisit(M,start_v)
    return True,cycle[::-1]

#testy
G=[[1,6],[0,2],[1,3,6],[2,4,5],[3,5],[3,4],[0,2,7],[6]]
print(EulerCycle(G,1))
G=[[1,3],[0,2],[1,3],[0,2]]
print(EulerCycle(G,3))
G=[[1,2],[0,2,3,4,5,6],[0,1,3,4,5,6],[1,2,4,5],[1,2,3,5],[1,2,3,4],[1,2]]
print(EulerCycle(G,0))
G=[[1,8],[0,2],[1,3],[2,4],[3,5,7],[4,6],[5,7],[4,6,8],[7,0]]
print(EulerCycle(G,8))
