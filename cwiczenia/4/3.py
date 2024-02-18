#Dana jest tablica n liczb. Szukamy takich dwóch,
#które po posortowaniu byłyby koło siebie, a różnica 
#jest maksymalna. Pomysł: wyszukujemy max i min
#w tablicy, tworzymy n kubełków (każdy obejmuje
#przedział (max-min) / n), szukamy różnicy między
#min. kubełka a maks. kubełka, pomiędzy którymi jest
#najwięcej pustych. Jeżeli takich nie ma, to po
#prostu liniowo badamy różnicę.

from random import randint

#zadanie 3
def max_diff(A):
    #min_max z zad 3 cw 1
    n=len(A)
    maxi=mini=A[-1]
    for i in range(1,n,2):
        if A[i]<A[i-1]:
            mi,ma=A[i],A[i-1]
        else:
            mi,ma=A[i-1],A[i]
        maxi=max(maxi,ma)
        mini=min(mini,mi)
    T=[[] for _ in range(n+1)]
    for i in range(n):
        T[int(n*(A[i]-mini)/(maxi-mini))].append(A[i])
    interval_start=[]
    max_interval_length=[-1]
    curr_interval_length=0
    for i in range(1,n+1):
        if T[i]==[]:
            curr_interval_length+=1
        else:
            if max_interval_length[-1]<curr_interval_length:
                max_interval_length=[curr_interval_length]
                interval_start=[i-max_interval_length[-1]-1]
            elif max_interval_length[-1]==curr_interval_length:
                max_interval_length.append(curr_interval_length)
                interval_start.append(i-max_interval_length[-1]-1)
            curr_interval_length=0
    a=max(T[interval_start[0]]),min(T[interval_start[0]+max_interval_length[0]+1])
    max_dif=a[1]-a[0]
    for i in range(1,len(max_interval_length)):
        b=max(T[interval_start[i]]),min(T[interval_start[i]+max_interval_length[i]+1])
        if b[1]-b[0]>max_dif:
            max_dif=b[1]-b[0]
            a=b
    return a

#testy
T=[randint(0,100) for _ in range(20)]
print(*sorted(T))
print(max_diff(T))
