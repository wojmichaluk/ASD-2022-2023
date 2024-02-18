from BST_and_RB_tree import *
from queue import deque
from math import ceil,log2

#drzewo przedziałowe, wykorzystuje BST z wykładu 14        
def create_tree(intervals):
    n=len(intervals)
    if not n: return
    T=[intervals[i//2][i%2] for i in range(2*n)]
    T=sorted(set(T))
    height=ceil(log2(len(T)+1))
    while len(T)<2**height-1:
        T.append(T[-1]+1)
    root=BSTNode(T[(len(T)-1)//2])
    Q1=deque()
    Q1.append((root,0,len(T)))
    Q2=deque()
    while len(Q1):
        node,beg,end=Q1.popleft()
        mid=(beg+end)//2
        left=insert(root,T[(beg+mid)//2])
        right=insert(root,T[(mid+end)//2])
        if left: Q1.append((left,beg,mid))
        else:
            left=BSTNode()
            Q2.append(left)
            left.parent=node
            node.left=left
        if right: Q1.append((right,mid,end))
        else:
            right=BSTNode()
            Q2.append(right)
            right.parent=node
            node.right=right
    index=0
    while len(Q2):
        leaf=Q2.popleft()
        Q1.append(leaf.parent)
        if leaf.parent.key==T[0] and leaf==leaf.parent.left:
            leaf.span=(-float('inf'),T[0])
        elif leaf.parent.key==T[-1] and leaf==leaf.parent.right:
            leaf.span=(T[-1],float('inf'))
        else:
            leaf.span=(T[index],T[index+1])
            index+=1
    while len(Q1):
        node=Q1.popleft()
        if node.span: continue
        if node.left and node.right:
            node.span=(node.left.span[0],node.right.span[1])
        elif node.left: node.span=node.left.span
        else: node.span=node.right.span
        if node.parent: Q1.append(node.parent)
    return root

def show_tree(root):
    Q=deque()
    Q.append((root,0))
    curr_level=-1
    while len(Q):
        node,level=Q.popleft()
        if level!=curr_level:
            curr_level=level
            print('\n',level,':',sep='')
        print(node.key,node.span,end='\t')
        if node.left: Q.append((node.left,level+1))
        if node.right: Q.append((node.right,level+1))

#struktura z update oraz sum
class MODNode: #modified BSTNode
    def __init__(self,value):
        self.left=None
        self.right=None
        self.parent=None
        self.value=value
        self.indexes_span=None

def associated_with_table(T):
    root=create_tree(T)
    pass

def create_tree(A):
    n=len(A)
    end_level=ceil(log2(n))
    root=MODNode()
    Q1=deque()
    Q1.append((root,1))
    Q2=deque()
    curr_index=0
    while curr_index<n:
        node,level=Q.popleft()
        left=MODNode()
        left.parent=parent
        node.left=left
        if level==end_level:
            Q2.append(parent)
            left.value=A[curr_index]
            left.indexes_span=(curr_index,curr_index)
            curr_index+=1
        else: Q1.append((left,level+1))
        if curr_index==n: break
        right=MODNode()
        right.parent=parent
        node.right=right
        if level==end_level:
            right.value=A[curr_index]
            right.indexes_span=(curr_index,curr_index)
            curr_index+=1
        else: Q1.append((right,level+1))
    while len(Q2):
        node=Q2.popleft()
        if node.left and node.right:
            node.value=node.left.value+node.right.value
            node.indexes_span=(node.left.indexes_span[0],node.right.indexes_span[1])
        else:
            node.value=node.left.value
            node.indexes_span=node.left.indexes_span
        if node.parent and node.parent.left==node:
            Q2.append(node.parent)
    return root

def update():
    pass

def sum():
    pass

#spadające klocki
#v1 - drzewo przedziałowe


#v2 - drzewo czerwono-czarne


#testy
intervals=[(0,15),(5,20),(7,12),(5,10),(10,12)]
root=create_tree(intervals)
show_tree(root)
intervals=[(0,2),(1,3),(4,6),(5,7),(8,10),(9,11),(12,14),(13,15),(16,18),(17,17)]
root=create_tree(intervals)
show_tree(root)
T=[]
associated_with_table(T)
T=[]
associated_with_table(T)
