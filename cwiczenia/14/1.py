#Problem stacji benzynowych - jedziemy
#z miasta A do miasta B, A jest na pozycji
#0, B na pozycji n-1. Spalanie 1l/1km, w baku
#mieści się L litrów. Na niektórych pozycjach
#są stacje benzynowe. a) chcemy, by łączna liczba
#tankowań była minimalna. b) chcemy minimalnego
#kosztu, każda stacja ma cenę za 1l, w każdej stacji
#możemy tankować dowolną ilość paliwa. c) jak w b), ale
#musimy tankowac do pełna. 

from random import randint
from queue import PriorityQueue

#zadanie 1
def tank(stations,L): #1a)
    n=len(stations)
    far=[0]
    tanks=1
    pos=0
    while pos<n-L:
        pos+=L
        while not stations[pos]:
            pos-=1
        far.append(pos)
        tanks+=1
    return tanks,far

def travel(stations,costs,L): #1b)
    n=len(costs)
    existing_stations=[]
    for i in range(n):
        if stations[i]:
            existing_stations.append(i)
    if not stations[-1]: existing_stations.append(n-1)
    G=[]
    m=len(existing_stations)
    for i in range(m):
        G.append([[],costs[existing_stations[i]]])
        for j in range(i+1,m):
            G[-1][0].append((j,existing_stations[j]-existing_stations[i]))          
    DP=[[float('inf') for _ in range(L+1)] for _ in range(m)]
    q=PriorityQueue()
    q.put((0,0,0))
    while not q.empty():
        c,f,v=q.get()
        for i in range(L+1-f):
            if c+i*G[v][1]<DP[v][i+f]:
                DP[v][i+f]=c+i*G[v][1]
                for u,e in G[v][0]:
                    if i+f>=e:
                        q.put((c+i*G[v][1],i+f-e,u))
    return DP[m-1][0]

def full_tank(stations,costs,L): #1c)
    n=len(costs)
    cost=L*costs[0]
    i=1
    while i<n-L:
        min_ind=min_cost(costs,i,min(i+L-1,n-1))
        cost+=(min_ind-i+1)*costs[min_ind]
        i=min_ind+1
    return cost

def min_cost(costs,b,e):
    min_ind=len(costs)
    min_val=float('inf')
    for i in range(b,e+1):
        if costs[i] and costs[i]<=min_val:
            min_val=costs[i]
            min_ind=i
    return min_ind

#testy
stations=[1,0,1,0,1,0,0,1,0,0]
costs=[5,0,3,0,1,0,0,4,0,0]
L=4
print(stations,costs,sep='\n')
print(tank(stations,L))
print(travel(stations,costs,L))
print(full_tank(stations,costs,L))
stations=[randint(0,4)//4 for _ in range(20)]
costs=[0 for _ in range(20)]
for i in range(20):
    if i%5==0: stations[i]=1
    if stations[i]: costs[i]=randint(1,6)
L=8
print(stations,costs,sep='\n')
print(tank(stations,L))
print(travel(stations,costs,L))
print(full_tank(stations,costs,L))
