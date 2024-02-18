from BST_and_RB_tree import *
from random import randint

#lista jednokierunkowa
class SNode:
    def __init__(self,val=None):
        self.next=None
        self.val=val

#lista dwukierunkowa
class DNode:
    def __init__(self,val=None):
        self.prev=None
        self.next=None
        self.val=val

#stos
#implementacja tablicowa
class StackA:
    def __init__(self):
        self.A=[]
        self.size=0

def pushA(stack,x):
    stack.A.append(x)
    stack.size+=1

def popA(stack):
    if not stack.size: return None
    ret=stack.A.pop()
    stack.size-=1
    return ret

def isemptyA(stack):
    return not stack.size

#implementacja listowa 
class StackL:
    def __init__(self):
        self.top=None
        self.size=0

def pushL(stack,x):
    if not stack.size: stack.top=SNode(x)
    else:
        s=SNode(x)
        s.next=stack.top
        stack.top=s
    stack.size+=1

def popL(stack):
    if not stack.size: return None
    ret=stack.top.val
    stack.top=stack.top.next
    stack.size-=1
    return ret

def isemptyL(stack):
    return not stack.size

#kolejka
#implementacja tablicowa
class QueueA:
    def __init__(self):
        self.A=[None for _ in range(4)]
        self.size=0
        self.head=0
        self.tail=0

def putA(queue,x):
    if queue.size:
        if (queue.tail+1)%len(queue.A)==queue.head:
            T=[0 for _ in range(queue.size*2)]
            for i in range(queue.size):
                T[i]=queue.A[(queue.head+i)%queue.size]
            queue.A=T
            queue.head=0
            queue.tail=queue.size
        else:
            queue.tail=(queue.tail+1)%len(queue.A)
    queue.A[queue.tail]=x
    queue.size+=1

def getA(queue):
    if not queue.size: return None
    ret=queue.A[queue.head]
    queue.size-=1
    queue.head=(queue.head+1)%len(queue.A)
    return ret

def q_isemptyA(queue):
    return not queue.size

#implementacja listowa
class QueueL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

def putL(queue,x):
    if not queue.size:
        queue.head=queue.tail=SNode(x)
    else:
        q=SNode(x)
        queue.tail.next=q
        queue.tail=q
    queue.size+=1

def getL(queue):
    if not queue.size: return None
    ret=queue.head.val
    queue.head=queue.head.next
    if not queue.head: queue.tail=None
    queue.size-=1
    return ret

def q_isemptyL(queue):
    return not queue.size

#kolejka priorytetowa
#implementacja na kopcu binarnym
class BinaryHeap:
    def __init__(self):
        self.T=[]

def insert(H,x,data):
    n=len(H.T)
    H.T.append((x,data))
    i=n
    p=(i-1)//2
    while p>=0:
        if H.T[p][0]>=H.T[i][0]: break
        H.T[p],H.T[i]=H.T[i],H.T[p]
        i=p
        p=(i-1)//2

def extract_max(H):
    if not len(H.T): return None
    ret=H.T[0][1]
    H.T[0],H.T[-1]=H.T[-1],H.T[0]
    H.T.pop()
    heapify_down(H.T,0,len(H.T))
    return ret

#pomocnicza do extract_max
def heapify_down(T,i,n):
    l=2*i+1
    r=2*i+2
    max_ind=i
    if l<n and T[l][0]>T[max_ind][0]:
        max_ind=l
    if r<n and T[r][0]>T[max_ind][0]:
        max_ind=r
    if max_ind!=i:
        T[i],T[max_ind]=T[max_ind],T[i]
        heapify_down(T,max_ind,n)

def decrease_key(H,key,dec_rate):
    ind=ind_search(H.T,key)
    if ind==None: return
    data=H.T[ind][1]
    H.T[ind],H.T[-1]=H.T[-1],H.T[ind]
    H.T.pop()
    heapify_down(H.T,ind,len(H.T))
    insert(H,key-dec_rate,data)

#pomocnicza do decrease_key
def ind_search(T,key):
    for i in range(len(T)):
        if T[i][0]==key: return i

#słownik
pass

#testy
Stack=StackA()
for i in range(10): pushA(Stack,i+1)
for i in range(12): print(popA(Stack),isemptyA(Stack),end=' ')
print('\n')
Stack=StackL()
for i in range(5): pushL(Stack,i+1)
for i in range(3): print(popL(Stack),isemptyL(Stack),end=' ')
print()
for i in range(10): pushL(Stack,i+3)
for i in range(15): print(popL(Stack),isemptyL(Stack),end=' ')
print('\n')
Queue=QueueA()
for i in range(10): putA(Queue,i+1)
for i in range(12): print(getA(Queue),q_isemptyA(Queue),end=' ')
print('\n')
Queue=QueueL()
for i in range(5): putL(Queue,i+1)
for i in range(3): print(getL(Queue),q_isemptyL(Queue),end=' ')
print()
for i in range(10): putL(Queue,i+6)
for i in range(15): print(getL(Queue),q_isemptyL(Queue),end=' ')
print('\n')
H=BinaryHeap()
for i in range(15): insert(H,randint(11,100),"element no "+str(i+1))
T=sorted(H.T,reverse=True)
print(T,'\n')
for i in range(15):
    decrease_key(H,T[i][0]+90*(i%2),10)
    T[i]=(T[i][0]-((i+1)%2)*10,T[i][1])
print(T,'\n')
for i in range(20): print(extract_max(H))
