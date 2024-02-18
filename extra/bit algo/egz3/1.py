from zad1testy import runtests

#zadanie 1
def rect(D):
    n=len(D)
    L=[(0,0,0,0) for _ in range(n)]
    R=[(0,0,0,0) for _ in range(n)]
    L[0]=(-float('inf'),-float('inf'),float('inf'),float('inf'))
    R[n-1]=(-float('inf'),-float('inf'),float('inf'),float('inf'))
    for i in range(n-1):
        L[i+1]=intersect(L[i],D[i])
        R[n-i-2]=intersect(R[n-i-1],D[n-i-1])
    max_area=0
    max_ind=-1
    for i in range(n):
        curr_area=area(intersect(L[i],R[i]))
        if curr_area>max_area:
            max_area=curr_area
            max_ind=i
    return max_ind
    
def intersect(a1,a2):
    ld1=max(a1[0],a2[0])
    ld2=max(a1[1],a2[1])
    pg1=min(a1[2],a2[2])
    pg2=min(a1[3],a2[3])
    if pg1<=ld1 or pg2<=ld2: return (0,0,0,0)
    return (ld1,ld2,pg1,pg2)

def area(rec):
    return (rec[2]-rec[0])*(rec[3]-rec[1])

#testy
runtests( rect )
