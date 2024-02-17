#Wojciech Michaluk
#Algorytm najpierw wyznacza tablicę plam ropy (elementy
#zawierają informacje o objętości plamy oraz indeksie
#kolumny, gdzie plama się zaczyna). Następnie, jadąc w
#stronę pola docelowego, szuka w zakresie pól, dokąd
#jesteśmy w stanie dojechać, plamy o największej objętości,
#dodaje tę objętość do łącznie zebranego paliwa i "zeruje"
#plamę (nie ma znaczenia, czy najpierw uwzględnimy plamę
#o objętości np. 3, a poźniej 4 czy odwrotnie - jeżeli można
#dojechać, choć zbieranie na trasie odbywałoby się oczywiście
#po kolei). Szacuję złożoność czasową algorytmu na O(nm+n^2),
#z kolei pamięciową na O(nm).

from zad8testy import runtests
from collections import deque

def plan(T):
    m=len(T[0])-1
    spills=get_spills(T)
    n=len(spills)
    curr_fuel=spills[0][1]
    spills[0]=(spills[0][0],0)
    stops=1
    while(curr_fuel<m):
        maks=0
        maks_ind=-1
        for i in range(n):
            if spills[i][0]>curr_fuel: break
            if spills[i][1]>maks:
                maks=spills[i][1]
                maks_ind=i
        curr_fuel+=maks
        spills[maks_ind]=(spills[maks_ind][0],0)
        stops+=1
    return stops

def get_spills(M):
    n=len(M)
    m=len(M[0])
    vis=[[0 for _ in range(m)] for _ in range(n)]
    q=deque()
    spills=[]
    for i in range(m):
        if not vis[0][i] and M[0][i]:
            vis[0][i]=1
            q.append((0,i))
            curr_spill=M[0][i]
            while q:
                x,y=q.pop()
                curr_spill+=try_moving_to(x-1,y,n,m,vis,M,q)
                curr_spill+=try_moving_to(x+1,y,n,m,vis,M,q)
                curr_spill+=try_moving_to(x,y-1,n,m,vis,M,q)
                curr_spill+=try_moving_to(x,y+1,n,m,vis,M,q)
            spills.append((i,curr_spill))
    return spills

def try_moving_to(x,y,n,m,vis,M,q):
    if 0<=x<n and 0<=y<m and not vis[x][y] and M[x][y]:
        vis[x][y]=1
        q.append((x,y))
        return M[x][y]
    return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )
