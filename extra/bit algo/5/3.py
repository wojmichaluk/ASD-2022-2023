#zadanie 3
def check_if_mst(E,T,d):
    #E jest przydatne np. do wyznaczenia Dijkstrą
    #tablicy odległości d,tutaj mamy tablicę d daną
    for e in T:
        f,t,w=e
        if d[f]+w>d[t]:
            return False
    return True

#testy
E=[(0,1,6),(0,4,2),(1,0,6),(1,2,4),(1,3,5),(1,4,3),(2,1,4),
(2,3,8),(2,4,7),(3,1,5),(3,2,8),(4,0,2),(4,1,3),(4,2,7)]
T=[(0,4,2),(4,1,3),(1,2,4),(1,3,5)]
d=[0,5,9,10,2]
print(check_if_mst(E,T,d))
E=[(0,1,3),(0,2,2),(0,3,6),(1,0,3),(1,2,4),(1,3,7),
(2,0,2),(2,1,4),(2,3,5),(3,0,6),(3,1,7),(3,2,5)]
T=[(0,1,3),(1,2,4),(2,3,5)]
d=[0,3,2,6]
print(check_if_mst(E,T,d))
E=[(0,1,14),(0,2,7),(0,3,11),(0,4,12),(0,5,9),(1,0,14),(1,2,8),(1,4,17),
(2,0,7),(2,1,8),(2,3,13),(3,0,11),(3,2,13),(4,0,12),(4,1,17),(5,0,9)]
T=[(0,1,14),(0,2,7),(0,3,11),(0,4,12),(0,5,9)]
d=[0,14,7,11,12,9]
print(check_if_mst(E,T,d))
