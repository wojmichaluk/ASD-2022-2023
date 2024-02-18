#Eksperyment fizyczny - generujemy wartości od 0
#do 10^9 - 1. Generujemy serię, należy w czasie
#stałym powiedzieć, ile różnych wartości się pojawiło.
#Pomysł: wykorzystujemy tablicę "liczników" i stos.
#Liczba różnych elementów to rozmiar stosu, zerowanie
#stosu: S=[].

from random import randint

#zadanie 6
class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def experiment(L,n):
    S=[]
    for i in range(n):
        k=randint(0,10**2-1)
        if L[k][0].next and L[k][0].next[1].next==S:
            L[k]=(L[k][0],L[k][1]+1)
        else:
            S.append((k,Node(None)))
            L[k][0].next=S[-1]
            S[-1][1].next=S
            L[k]=(L[k][0],1)
    return len(S)

#testy
L=[(Node(i),0) for i in range(10**2)]
print(experiment(L,50))
#for i in range(len(L)):
#    print(L[i][1],end=' ')
#print()
print(experiment(L,50))
#for i in range(len(L)):
#    print(L[i][1],end=' ')
#print()
