#niepokrywające się przedziały
def tasks(T):
    T.sort(key=lambda x: x[1])
    n=len(T)
    last_end=0
    no_tasks=0
    chosen_tasks=[]
    for i in range(n):
        if T[i][0]>=last_end:
            no_tasks+=1
            chosen_tasks.append(T[i])
            last_end=T[i][1]
    return no_tasks,chosen_tasks

#kod Huffmana
def huff(T):
    T.sort(key=lambda x: x[1])
    n=len(T)
    codes=[[] for _ in range(n)]
    for i in range(n-1):
        if codes[T[1][0][0]]: mod=1
        else: mod=0
        for el in T[0][0]: codes[el].append(1-mod)
        for el in T[1][0]: codes[el].append(mod)
        new_el=(T[0][0]+T[1][0],T[0][1]+T[1][1])
        j=2
        while j<len(T):
            if new_el[1]<T[j][1]: break
            j+=1
        T=T[2:j]+[new_el]+T[j:]
    for i in range(n):
        codes[i].reverse()
    return codes

#problem plecakowy
#1)wersja ciągła
def knapsack(W,P,M):
    n=len(W)
    F=[(P[i]/W[i],W[i]) for i in range(n)]
    F.sort(reverse=True)
    cap_left=M
    value=0
    for i in range(n):
        if not cap_left: break
        m=min(cap_left,F[i][1])
        cap_left-=m
        value+=m*F[i][0]
    return value

#2)algorytmy zachłanne do wersji dyskretnej
def knapsackv1(W,P,M):
    n=len(W)
    F=[(P[i]/W[i],W[i]) for i in range(n)]
    F.sort(reverse=True)
    cap_left=M
    value=0
    for i in range(n):
        if not cap_left: break
        if cap_left<F[i][1]: m=0
        else: m=F[i][1]
        cap_left-=m
        value+=m*F[i][0]
    return value

def knapsackv2(W,P,M):
    n=len(W)
    F=[(P[i],W[i]) for i in range(n)]
    F.sort(reverse=True)
    cap_left=M
    value=0
    for i in range(n):
        if not cap_left: break
        if cap_left<F[i][1]: m=0
        else: m=F[i][1]
        cap_left-=m
        value+=F[i][0]
    return value

#testy
T=[(0,3),(2,5),(7,10),(9,11),(13,17),(2,8),(12,14),(10,15),(16,19)]
print(tasks(T))
T=[(0,7),(1,4),(6,12),(11,13),(9,14),(4,8),(15,19),(17,20),(13,16),(18,21)]
print(tasks(T))
T=[([0],700),([1],200),([2],120),([3],300),([4],10)]
print(huff(T))
T=[([0],50),([1],5),([2],60),([3],65),([4],20)]
print(huff(T))
P=[60,75,65,120,150]
W=[2,3,5,8,3]
print(knapsack(W,P,6))
P=[22,15,20,32,17,41]
W=[4,3,6,8,4,12]
print(knapsack(W,P,10))
P=[70,55,35]
W=[70,60,40]
print(knapsackv1(W,P,100))
P=[2,9]
W=[2,10]
print(knapsackv1(W,P,10))
P=[2,1,1,1,1,1]
W=[5,1,1,1,1,1]
print(knapsackv2(W,P,5))
P=[3,1,1,1,1,1]
W=[4,1,1,1,1,1]
print(knapsackv2(W,P,5))
