#zadanie 3
class Node:
    def __init__(self):
        self.left=None
        self.leftval=0
        self.right=None
        self.rightval=0
        self.X=None

def valuableTree(T,k):
    set_x(T,k)
    curr_max=[0]
    find_best(T,k,curr_max)
    return curr_max[0]

def set_x(T,k):
    T.X=[None for _ in range(k+1)]
    if T.left!=None:
        set_x(T.left,k)
    if T.right!=None:
        set_x(T.right,k)

def find_best(T,k,curr_max):
    curr_max[0]=max(curr_max[0],rek(T,k))
    if T.left!=None:
        find_best(T.left,k,curr_max)
    if T.right!=None:
        find_best(T.right,k,curr_max)

def rek(T,k):
    if T==None: return -float('inf')
    if T.X[k]!=None: return T.X[k]
    if k==0:
        T.X[k]=0
        return T.X[k]
    mixed_max=-float('inf')
    for j in range(1,k):
        mixed_max=max(mixed_max,rek(T.left,j-1)+T.leftval+rek(T.right,k-j-1)+T.rightval)
    T.X[k]=max(rek(T.left,k-1)+T.leftval,rek(T.right,k-1)+T.rightval,mixed_max)
    return T.X[k]

#testy
A=Node(); B=Node(); C=Node(); D=Node(); E=Node(); F=Node(); G=Node();
A.left=B; A.leftval=1; A.right=E; A.rightval=5
B.left=D; B.leftval=6; B.right=C; B.rightval=2
C.left=F; C.leftval=8; C.right=G; C.rightval=10
print(valuableTree(A,3))
print(valuableTree(A,4))
A=Node(); B=Node(); C=Node(); 
D=Node(); E=Node(); F=Node(); 
G=Node(); H=Node(); I=Node();
A.left=B; A.leftval=7; A.right=C; A.rightval=6
B.left=D; B.leftval=3; B.right=E; B.rightval=5
C.left=F; C.leftval=4; E.left=G; E.leftval=2
E.right=H; E.rightval=9; F.right=I; F.rightval=3
print(valuableTree(A,5))
print(valuableTree(A,6))
