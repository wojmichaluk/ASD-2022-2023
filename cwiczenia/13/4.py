#Głodna żaba - żaba skacze po osi liczbowej,
#skacze od 0 do n-1 wyłącznie w kierunku
#większych liczb, ale jej energia nie może
#spaść poniżej zera.

#zadanie 4
def zew(A):
    n=len(A)-1
    snacks=[]
    for i in range(n+1):
        if A[i]: snacks.append((i,A[i]))
    snacks.append((n,0))
    m=len(snacks)
    def rek(T,fuel=0,i=0,s=0): #rekurencyjnie
        if fuel<0: return float('inf')
        if i==len(T)-1: return s
        dist=T[i+1][0]-T[i][0]
        return min(rek(T,fuel-dist,i+1,s),rek(T,fuel-dist+T[i][1],i+1,s+1))
    return rek(snacks)

def frog(A): #dynamik
    n=len(A)-1
    snacks=[]
    for i in range(n+1):
        if A[i]: snacks.append((i,A[i]))
    m=len(snacks)
    curr_energy=snacks[0][1]
    snacks[0]=(snacks[0][0],0)
    stops=1
    while(curr_energy<n):
        maks=0
        maks_ind=-1
        for i in range(m):
            if snacks[i][0]>curr_energy: break
            if snacks[i][1]>maks:
                maks=snacks[i][1]
                maks_ind=i
        curr_energy+=maks
        snacks[maks_ind]=(snacks[maks_ind][0],0)
        stops+=1
    return stops

#testy
A=[1,0]
print(zew(A))
print(frog(A))
A=[3,0,1,4,0,2,0,5,1,0,1,0,0]
print(zew(A))
print(frog(A))
A=[2,1,3,0,0,0,5,0,2,0]
print(zew(A))
print(frog(A))
