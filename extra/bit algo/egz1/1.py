from egz1btesty import runtests

#zadanie 1

class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.x=None

def widentall( T ):
    h_max=[0]
    set_x(T,0,h_max)
    H=[0 for _ in range(h_max[0]+1)]
    set_htable(H,T)
    return find_best(H,T)

def set_x(T,h,h_max):
    T.x=h
    if h>h_max[0]: h_max[0]=h
    if T.left!=None: set_x(T.left,h+1,h_max)
    if T.right!=None: set_x(T.right,h+1,h_max)

def set_htable(H,T):
    H[T.x]+=1
    if T.left!=None: set_htable(H,T.left)
    if T.right!=None: set_htable(H,T.right)

def find_best(H,T):
    h=len(H)
    index=0
    max_nodes=0
    for i in range(h):
        if H[i]>=max_nodes:
            max_nodes=H[i]
            index=i
    to_del=[0]
    if index<h-1: to_del[0]=H[index+1]
    reset_x(T,index)
    cut_leaves_above(T,to_del,index)
    return to_del[0]
    
def reset_x(T,i):
    T.x=(T.x,1,0)
    if T.x[0]==i:
        return (0,1)
    elif T.left==T.right==None:
        return (1,0)
    a=b=c=d=0
    if T.left: a,b=reset_x(T.left,i)
    if T.right: c,d=reset_x(T.right,i)
    T.x=(T.x[0],a+c,b+d)
    return (a+c,b+d)
    
def cut_leaves_above(T,to_del,i):
    if T.x[0]==i-1: return
    if T.left and T.left.x[1] and T.left.x[2]==0:
        to_del[0]+=1
    elif T.left: cut_leaves_above(T.left,to_del,i)
    if T.right and T.right.x[1] and T.right.x[2]==0:
        to_del[0]+=1
    elif T.right: cut_leaves_above(T.right,to_del,i)

#testy
runtests( widentall, all_tests = True ) 
