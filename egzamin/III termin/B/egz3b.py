#Wojciech Michaluk
#...
#no niestety nie działa to O(nlogn)

from egz3btesty import runtests
"""
from queue import deque
from math import log2,ceil

def uncool( P ):
    n=len(P)
    int_points=[P[i//2][i%2] for i in range(2*n)]
    int_points.sort()
    unique_points=[int_points[0]]
    last=int_points[0]
    for i in range(1,2*n):
        if int_points[i]!=last:
            unique_points.append(int_points[i])
            last=int_points[i]
    root=create_tree(unique_points)
    containing_nodes=[[] for _ in range(n)]
    for i in range(n):
        fill_tree(root,P[i][0],P[i][1],i,containing_nodes)
    for i in range(n):
        for j in range(len(containing_nodes[i])):
            found=go_up(P,containing_nodes,containing_nodes[i][j],i)
            if found: return (i,found)

class Node:
    def __init__(self):
        self.parent=None
        self.left=None
        self.right=None
        self.contained_intervals=[]
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

def fill_tree(root,l,r,index,table):
    Q=deque()
    Q.append((root,l,r))
    while len(Q):
        node,le,ri=Q.popleft()
        if node.interval==(le,ri):
            node.contained_intervals+=[index]
            table[index]+=[node]
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
    return [beg,end]

def go_up(P,table,node,index):
    start=node
    while start:
        n=len(start.contained_intervals)
        for i in range(n):
            if start.contained_intervals[i]!=index:
                if not inside(P[index],P[start.contained_intervals[i]]) and len(table[index])>1:
                    return start.contained_intervals[i]
        start=start.parent

def inside(p1,p2):
    interval=intersect(p1,p2[0],p2[1])
    return interval==p1 or interval==p2

"""
#Wojciech Michaluk
#Algorytm sprawdza po kolei każdą
#parę przedziałów, badając, czy są
#"fajne" - zgodnie z definicją podaną
#w poleceniu; w przypadku gdy
#znajdzie niefajną parę, zwraca indeksy
#przedziałów z tej pary. Złożoność
#czasową algorytmu szacuję na O(n^2),
#a pamięciową na O(1).

#O(n^2)
def uncool( P ):
    n=len(P)
    for i in range(n-1):
        for j in range(i+1,n):
            if not iscool(P[i],P[j]): return (i,j)

def iscool(p1,p2):
    return disjunct(p1,p2) or includes(p1,p2) or includes(p2,p1)

def disjunct(p1,p2):
    return max(p1[0],p2[0])>min(p1[1],p2[1])

def includes(p1,p2):
    return p1[0]>=p2[0] and p1[1]<=p2[1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True)
