from queue import PriorityQueue

#zadanie 5

def jumper(G,s,w):
    n=len(G)
    Gr=[[] for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]:
                Gr[3*i].append((3*j,G[i][j]))
                Gr[3*i].append((3*j+2,G[i][j]))
                Gr[3*i+1].append((3*j,G[i][j]))
                Gr[3*i+2].append((3*j+1,G[i][j]))
    d=[float('inf') for _ in range(3*n)]
    d[3*s]=0
    q=PriorityQueue()
    q.put((0,3*s,0,0))
    while not q.empty():
        p,u,l,prev=q.get()
        if p==d[u]:
            for v,c in Gr[u]:
                if u%3==2:
                    if relax(prev,d,v,max(c,l)):
                        q.put((d[v],v,c,u))
                elif relax(u,d,v,c):
                    q.put((d[v],v,c,u))
    return min(d[3*w],d[3*w+1],d[3*w+2])

def relax(u,d,v,c):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        return True
    return False

#testy
G=[[0,1,0,0,0],[1,0,1,0,0],[0,1,0,7,0],[0,0,7,0,8],[0,0,0,8,0]]
print(jumper(G,0,4))
G=[[0,2,0,0,0,0],[2,0,7,0,0,0],[0,7,0,4,0,0],
[0,0,4,0,5,0],[0,0,0,5,0,6],[0,0,0,0,6,0]]
print(jumper(G,0,5))
G=[[0,3,7,0,0,0],[3,0,0,5,6,9],[7,0,0,4,0,0],
[0,5,4,0,0,0],[0,6,0,0,0,8],[0,9,0,0,8,0]]
print(jumper(G,2,4))
