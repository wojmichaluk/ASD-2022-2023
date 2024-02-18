#zadanie 6
def min_alpha(S):
    cnt=[0 for _ in range(ord('z')-ord('a')+1)]
    V=[False for _ in range(ord('z')-ord('a')+1)]
    new_word=[]
    for c in S:
        cnt[ord(c)-97]+=1
    stack=Stack()
    for c in S:
        ind=ord(c)-97
        take_from_stack(ind,stack,cnt,V)
        if not V[ind]:
            push(stack,c)
            V[ind]=True
        cnt[ind]-=1
    res=""
    for i in range(len(stack.A)):
        res+=stack.A[i]
    return res

def take_from_stack(ind,stack,cnt,V):
    while not isempty(stack):
        taken=pop(stack)
        temp_ind=ord(taken)-97
        if temp_ind<ind or (temp_ind>ind and not cnt[temp_ind]):
            push(stack,taken)
            break
        V[temp_ind]=False
    
#stos, implementacja tablicowa
class Stack:
    def __init__(self):
        self.A=[]
        self.size=0

def push(stack,x):
    stack.A.append(x)
    stack.size+=1

def pop(stack):
    if not stack.size: return None
    ret=stack.A.pop()
    stack.size-=1
    return ret

def isempty(stack):
    return not stack.size

#testy
S="cbacdcbc"
print(min_alpha(S))
S="mamolubieplacki"
print(min_alpha(S))
S="hgfedcba"
print(min_alpha(S))
