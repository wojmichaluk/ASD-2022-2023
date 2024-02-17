#Wojciech Michaluk
#Z warunków zadania wynika, że wystarczy rozważyć n
#magazynów. Algorytm operuje na strukturze drzewa
#binarnego, w którym każdy liść (liście znajdują się na
#najniższym poziomie) odpowiada magazynowi i ma
#swoje id (nr magazynu), przechowuje również informacje
#o ilości przechowywanego węgla i jeszcze dostępnej
#pojemności. Po stworzeniu drzewa dla każdej dostawy
#rozważam minimalne id magazynu, który może pomieścić
#dostawę i aktualizuję dla danej gałęzi drzewa maksymalną
#dostępną pojemność. Szacuję złożoność czasową
#algorytmu na O(nlogn), a pamięciową na O(n).

from egz2atesty import runtests
from queue import PriorityQueue,deque
from math import log2,ceil

#O(nlogn), na podstawie kodu by Artur Gęsiarz
def coal( A, T ):
    n=len(A)
    root=create_tree(A,T)
    last=0
    for i in range(n):
        curr_coal=A[i]
        curr_node=search_in_tree(root,curr_coal)
        update_max(curr_node)
        last=curr_node.id
    return last

class Node:
    def __init__(self):
        self.level=0
        self.parent=None
        self.left=None
        self.right=None
        self.max=None
        self.id=None #tylko dla lisci
        self.curr_coal=0 #tylko dla lisci

def create_tree(A,T):
    n=len(A)
    nodes=2**(ceil(log2(n))+1)-1
    end_level=ceil(log2(n))
    curr_nodes=1
    root=Node()
    root.max=T
    Q=deque()
    Q.append(root)
    curr_id=0
    while curr_nodes!=nodes:
        father=Q.popleft()
        left=Node()
        left.parent=father
        left.level=left.parent.level+1
        left.max=T
        right=Node()
        right.parent=father
        right.level=right.parent.level+1
        right.max=T
        father.left=left
        father.right=right
        if left.level==end_level:
            left.id=curr_id
            right.id=curr_id+1
            curr_id+=2
        else:
            Q.append(left)
            Q.append(right)
        curr_nodes+=2
    return root

def search_in_tree(root,coal):
    node=root
    while node:
        if node.left==None and node.right==None:
            node.curr_coal+=coal
            node.max-=coal
            return node
        elif node.left!=None and node.left.max>=coal:
            node=node.left
        else: node=node.right

def update_max(node):
    v=node.parent
    while v:
        v.max=max(v.left.max,v.right.max)
        v=v.parent

"""
#Wojciech Michaluk
#Algorytm dla każdego z transportów przegląda
#wszystkie magazyny od pierwszego począwszy
#i jeżeli znajdzie magazyn mogący pomieścić
#dostawę, umieszcza tam węgiel (zmniejszając
#jego pozostałą dostępną pojemność). Złożoność
#czasową algorytmu szacuję na O(n^2), za to
#pamięciową na O(n).

#O(n^2)
def coal( A, T ):
    n=len(A)
    B=[T for _ in range(n)]
    for i in range(n-1):
        for j in range(n):
            if B[j]>=A[i]:
                B[j]-=A[i]
                break
    for i in range(n):
            if B[i]>=A[n-1]:
                B[i]-=A[n-1]
                return i
"""

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
