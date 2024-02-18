from queue import Queue

def graphify(A,a,b):
    min_a=A[0][0]
    max_b=A[0][1]
    n=len(A)
    for i in range(1,n):
        min_a=min(min_a,A[i][0])
        max_b=max(max_b,A[i][1])
    V=max_b-min_a+1
    move=-min_a
    if a<min_a or b>max_b: return False
    a,b=a+move,b+move
    B=[[] for _ in range(V)]
    for i in range(n):
        B[A[i][0]+move].append(A[i][1]+move)
    q=Queue()
    q.put(a)
    while not q.empty():
        v=q.get()
        if v==b: return True
        if v>b: return False
        for u in B[v]:
            q.put(u)
    return False
        
#testy
A=[(1,3),(-3,0),(5,7),(-5,2),(4,7),(1,5),(0,4),(2,5),(7,10)]
print(graphify(A,-5,10))
print(graphify(A,-3,6))
print(graphify(A,1,5))
print(graphify(A,0,7))
print(graphify(A,-2,8))
print(graphify(A,-3,5))
