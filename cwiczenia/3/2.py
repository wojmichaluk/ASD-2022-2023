#QuickSort bez rekurencji, z własnym stosem.

from random import randint

#zadanie 2
class Stack:
    def __init__(self):
        self.T=[]
        self.size=0

    def push(self,elem):
        self.T.append(elem)
        self.size+=1

    def pop(self):
        if self.size==0:
            return
        self.size-=1
        return self.T.pop()

    def isempty(self):
        return self.size==0
    
def QS_iter(A,p,r):
    St=Stack()
    St.push((p,r))
    while not St.isempty():
        a,b=St.pop()
        if b>a:
            q=partition(A,a,b)
            St.push((a,q-1))
            St.push((q+1,b))

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

#testy
T=[randint(1,100000) for _ in range(100000)]
print(*T[:20])
QS_iter(T,0,len(T)-1)
print(*T[:20])
