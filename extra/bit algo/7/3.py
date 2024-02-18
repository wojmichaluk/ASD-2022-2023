from zad3testy import runtests
from queue import PriorityQueue

#zadanie 3
def zbigniew(A):
    n=len(A)-1
    snacks=[]
    for i in range(n+1):
        if A[i]: snacks.append((i,A[i]))
    m=len(snacks)
    q=PriorityQueue()
    q.put(-snacks[0][1])
    stops=0
    last_ind=0
    curr_energy=0
    while(curr_energy<n):
        if q.empty(): return -1
        energy=q.get()
        curr_energy-=energy
        for i in range(last_ind+1,m):
            if snacks[i][0]>curr_energy: break
            last_ind=i
            q.put(-snacks[i][1])
        stops+=1
    return stops

#testy
A=[3,0,0,2,0,4,0,1,0,0,0,0]
print(zbigniew(A))
runtests( zbigniew )
