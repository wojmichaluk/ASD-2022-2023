#Mamy pojemniki z wodą, opisane poprzez współrzędne lewego górnego
#i prawego dolnego rogu. Traktujemy, że tworzą system naczyń
#połączonych. Wiemy, ile wody już wlano. Ile pojemników jest
#w pełni zalanych?

from heap_structure_and_heapsort import *

#zadanie 3
def HowManyFilled(A,water):
    n=len(A)
    T=[0 for _ in range(2*n)]
    for i in range(n):
        cur=A[i]
        w=cur[1][0]-cur[0][0]
        T[2*i]=(cur[1][1],w)
        T[2*i+1]=(cur[0][1],-1*w)
    heapsort(T)
    cur_water=0
    counter=0
    active_width=T[0][1]
    l=T[0][0]
    for element in T[1:]:
        h=element[0]
        w_ch=element[1]
        cur_water+=active_width*(h-l)
        if cur_water>water:
            break
        if w_ch<0:
            counter+=1
        active_width+=w_ch
        l=h
    return counter

#testy
A=[((1,18),(6,15)),((5,13),(9,7)),((10,15),(16,10)),((4,6),(12,3)),((14,8),(19,2))]
print(HowManyFilled(A,60))
