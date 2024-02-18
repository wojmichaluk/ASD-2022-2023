#Problem otoczki wypukłej - mamy zbiór punktów
#na płaszczyźnie, szukamy najmniejszego wielokąta,
#który zawiera wszystkie punkty. Pokazać, że nie da
#się szybciej niż O(nlogn). Pomysł: algorytm na
#otoczkę wypukłą musi posortować dane z dokładnością
#do przesunięcia.

from random import randint

#zadanie 7
def otoczka_wypukla(T):
    n=len(T)
    if n==0: return []
    elif n==1: return T
    L=[]
    def hull(A,B,S):
        n=len(S)
        nonlocal L
        if n==0: return
        elif n==1: L.append(S[0])
        else:
            max_el=S[0]
            max_dist=dist(A,B,S[0])
            for i in range(1,n):
                curr_dist=dist(A,B,S[i])
                if curr_dist>max_dist:
                    max_dist=curr_dist
                    max_el=S[i]
            L.append(max_el)
            if max_dist==0: return
            T1=[]
            T2=[]
            if max_el[0]==A[0] and max_el[1]<A[1]:
                a2=(max_el[1]-B[1])/(max_el[0]-B[0])
                b2=max_el[1]-a2*max_el[0]
                for i in range(n):
                    line2=a2*S[i][0]+b2
                    if S[i][0]<A[0]: T1.append(S[i])
                    elif S[i][1]<line2: T2.append(S[i])
            elif max_el[0]==A[0] and max_el[1]>A[1]:
                a2=(max_el[1]-B[1])/(max_el[0]-B[0])
                b2=max_el[1]-a2*max_el[0]
                for i in range(n):
                    line2=a2*S[i][0]+b2
                    if S[i][0]<A[0]: T1.append(S[i])
                    elif S[i][1]>line2: T2.append(S[i])
            elif max_el[0]==B[0] and max_el[1]<B[1]:
                a1=(max_el[1]-A[1])/(max_el[0]-A[0])
                b1=max_el[1]-a1*max_el[0]
                for i in range(n):
                    line1=a1*S[i][0]+b1
                    if S[i][0]>B[0]: T2.append(S[i])
                    elif S[i][1]<line1: T1.append(S[i])
            elif max_el[0]==B[0] and max_el[1]>B[1]:
                a1=(max_el[1]-A[1])/(max_el[0]-A[0])
                b1=max_el[1]-a1*max_el[0]
                for i in range(n):
                    line1=a1*S[i][0]+b1
                    if S[i][0]>B[0]: T2.append(S[i])
                    elif S[i][1]>line1: T1.append(S[i])
            else:
                a1=(max_el[1]-A[1])/(max_el[0]-A[0])
                b1=max_el[1]-a1*max_el[0]
                a2=(max_el[1]-B[1])/(max_el[0]-B[0])
                b2=max_el[1]-a2*max_el[0]
                if A[0]==B[0]:
                    if max_el[0]>A[0] and A[1]<B[1]:     
                        for i in range(n):
                            line1=a1*S[i][0]+b1
                            line2=a2*S[i][0]+b2
                            if S[i][1]<line1: T1.append(S[i])
                            elif S[i][1]>line2: T2.append(S[i])
                    if max_el[0]>A[0] and A[1]>B[1]:     
                        for i in range(n):
                            line1=a1*S[i][0]+b1
                            line2=a2*S[i][0]+b2
                            if S[i][1]>line1: T1.append(S[i])
                            elif S[i][1]<line2: T2.append(S[i])
                    if max_el[0]<A[0] and A[1]<B[1]:     
                        for i in range(n):
                            line1=a1*S[i][0]+b1
                            line2=a2*S[i][0]+b2
                            if S[i][1]<line1: T1.append(S[i])
                            elif S[i][1]>line2: T2.append(S[i])
                    if max_el[0]<A[0] and A[1]>B[1]:     
                        for i in range(n):
                            line1=a1*S[i][0]+b1
                            line2=a2*S[i][0]+b2
                            if S[i][1]>line1: T1.append(S[i])
                            elif S[i][1]<line2: T2.append(S[i]) 
                else:
                    a=(B[1]-A[1])/(B[0]-A[0])
                    b=B[1]-a*B[0]
                    line=a*max_el[0]+b
                    if max_el[1]>line:
                        for i in range(n):
                            line1=a1*S[i][0]+b1
                            line2=a2*S[i][0]+b2
                            if S[i][1]>line1: T1.append(S[i])
                            elif S[i][1]>line2: T2.append(S[i])
                    else:
                        for i in range(n):
                            line1=a1*S[i][0]+b1
                            line2=a2*S[i][0]+b2
                            if S[i][1]<line1: T1.append(S[i])
                            elif S[i][1]<line2: T2.append(S[i])
            if max_el[0]<A[0]:
                hull(max_el,A,T1)
                hull(max_el,B,T2)
            elif max_el[0]>B[0]:
                hull(A,max_el,T1)
                hull(B,max_el,T2)
            else:
                hull(A,max_el,T1)
                hull(max_el,B,T2)
    T1=[]
    T2=[]
    mi,ma=min_max(T)
    if ma[0]==mi[0]:
        return []
    a=(ma[1]-mi[1])/(ma[0]-mi[0])
    b=ma[1]-a*ma[0]
    L.append(mi)
    L.append(ma)
    for i in range(n):
        line=a*T[i][0]+b
        if T[i][1]>line: T2.append(T[i])
        elif T[i][1]<line: T1.append(T[i])
    hull(mi,ma,T1)
    hull(mi,ma,T2)
    return L
    
def dist(A,B,P):
    if B[0]==A[0]:
        a=1
        b=0
        C=-B[0]
    else:
        a=(B[1]-A[1])/(B[0]-A[0])
        b=-1
        C=B[1]-a*B[0]
    return abs(a*P[0]+b*P[1]+C)/(a**2+b**2)**0.5

#testy
def min_max(T):
    n=len(T)
    gus=zus=T[-1]
    for i in range(1,n,2):
        if T[i][0]<T[i-1][0]:
            mi,ma=T[i],T[i-1]
        else:
            mi,ma=T[i-1],T[i]
        if ma[0]>gus[0]:
            gus=ma
        if mi[0]<zus[0]:
            zus=mi
    return zus,gus

T=[(randint(0,10),randint(0,10)) for _ in range(10)]
print(*T)
T=otoczka_wypukla(T)
print(*T)
