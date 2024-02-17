#Wojciech Michaluk
#Algorytm operuje na strukturze drzewa
#binarnego przechowującego przedziały -
#liście to pojedyncze punkty, każdy inny węzeł
#odpowiada przedziałowi obejmującemu sumę
#przedziałów dzieci itd. W tym celu najpierw
#"wyłuskuje" pojedyncze punkty z przedziałów,
#następnie sortuje je i usuwa duplikaty. Potem
#buduje drzewo i rozważa każdy z przedziałów,
#zwiększając odpowiednio grubość śniegu.
#Końcowo zwraca maksymalną grubość. Szacuję
#złożoność czasową algorytmu na O(nlogn), a
#pamięciową na O(n).

from egz3atesty import runtests
from queue import deque
from math import log2,ceil

#O(nlogn)
def snow( T, I ):
    n=len(I)
    int_points=[I[i//2][i%2] for i in range(2*n)]
    int_points.sort()
    unique_points=[int_points[0]]
    last=int_points[0]
    for i in range(1,2*n):
        if int_points[i]!=last:
            unique_points.append(int_points[i])
            last=int_points[i]
    root=create_tree(unique_points)
    for i in range(n):
        let_it_snow(root,I[i][0],I[i][1])
    return find_max(root)

class Node:
    def __init__(self):
        self.parent=None
        self.left=None
        self.right=None
        self.snow_height=0
        self.interval=(None,None)
        self.is_leaf=0

def create_tree(A):
    n=len(A)
    end_level=ceil(log2(n))
    cnt=0
    root=Node()
    Q1=deque()
    Q1.append((root,0))
    Q2=deque()
    while cnt<n:
        father,level=Q1.popleft()
        left=Node()
        left.parent=father
        father.left=left
        if level+1==end_level:
            left.interval=(A[cnt],A[cnt])
            cnt+=1
            left.is_leaf=1
            Q2.append(father)
        else: Q1.append((left,level+1))
        if cnt==n: break
        right=Node()
        right.parent=father
        father.right=right
        if left.is_leaf:
            right.interval=(A[cnt],A[cnt])
            cnt+=1
            right.is_leaf=1
        else: Q1.append((right,level+1))
    while len(Q2):
        node=Q2.popleft()
        if node.left and node.right:
            if node.right.interval==(None,None):
                node.right=None
            else:
                node.interval=(node.left.interval[0],node.right.interval[1])
        elif node.left:
            node.interval=node.left.interval
        if node.parent and node.parent.left==node:
            Q2.append(node.parent)
    return root

def let_it_snow(root,l,r):
    Q=deque()
    Q.append((root,l,r))
    while len(Q):
        node,le,ri=Q.popleft()
        if node.interval==(le,ri):
            node.snow_height+=1
        else:
            left=node.left
            right=node.right
            a=intersect(left.interval,le,ri)
            if a: Q.append((left,a[0],a[1]))
            if right:
                a=intersect(right.interval,le,ri)
                if a: Q.append((right,a[0],a[1]))

def intersect(interval,left,right):
    beg=max(interval[0],left)
    end=min(interval[1],right)
    if beg>end: return False
    return (beg,end)

def find_max(root):
    max_height=0
    Q=deque()
    Q.append((root,0))
    while len(Q):
        node,height=Q.popleft()
        node.snow_height+=height
        if node.is_leaf and node.snow_height>max_height:
            max_height=node.snow_height
        else:   
            if node.left: Q.append((node.left,node.snow_height))
            if node.right: Q.append((node.right,node.snow_height))
    return max_height

"""
#Wojciech Michaluk
#Algorytm najpierw wyłuskuje pojedyncze
#punkty z przedziałów, następnie sortuje
#je i usuwa duplikaty. Potem przechodzi po
#tablicy z przedziałami, wyszukuje binarnie
#początek i koniec przedziału w posortowanej
#tablicy i w odpowiednich punktach zwiększa
#grubość śniegu (z rozpatrywanego przedziału).
#Szacuję złożoność czasową algorytmu na
#O(n^2), a pamięciową na O(n).

#O(n^2)
def snow( T, I ):
    n=len(I)
    int_points=[I[i//2][i%2] for i in range(2*n)]
    int_points.sort()
    unique_points=[int_points[0]]
    last=int_points[0]
    for i in range(1,2*n):
        if int_points[i]!=last:
            unique_points.append(int_points[i])
            last=int_points[i]
    m=len(unique_points)
    snow_height=[0 for _ in range(m)]
    for i in range(n):
        j=binary_search(unique_points,I[i][0],0,m-1)
        k=binary_search(unique_points,I[i][1],j,m-1)
        for l in range(j,k+1):
            snow_height[l]+=1
    return max(snow_height)

def binary_search(A,val,p,r):
    i=(p+r)//2
    if A[i]==val: return i
    elif A[i]<val: return binary_search(A,val,i+1,r)
    else: return binary_search(A,val,p,i-1)
"""

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
