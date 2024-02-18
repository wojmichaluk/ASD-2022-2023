#fibonacci rekurencyjnie
def fib_rek(n):
    if n<2: return 1
    return fib_rek(n-1)+fib_rek(n-2)

#fibonacci dynamicznie
def fib_dyn(n):
    F=[1]*(n+1)
    for i in range(2,n+1):
        F[i]=F[i-1]+F[i-2]
    return F[n]

#najdłuższy rosnący podciąg
def lis(A):
    n=len(A)
    F=[1]*n
    P=[-1]*n
    for i in range(1,n):
        for j in range(0,i):
            if A[j]<A[i] and F[j]+1>F[i]:
                P[i]=j
                F[i]=F[j]+1
    max_ind=0
    max_el=F[0]
    for i in range(1,n):
        if F[i]>max_el:
            max_el=F[i]
            max_ind=i
    return max_ind,P

#odtworzenie podciągu
def ps(A,P,i):
    if P[i]!=-1:
        ps(A,P,P[i])
    print(A[i],end=' ')

#impreza firmowa
class Employee:
    def __init__(self,fun):
        self.emp=[]
        self.fun=fun
        self.f=-1
        self.g=-1

def f(v):
    if v.f>=0: return v.f
    x=v.fun
    for ui in v.emp:
        x+=g(ui)
    y=g(v)
    v.f=max(x,y)
    return v.f

def g(v):
    if v.g>=0: return v.g
    x=0
    for ui in v.emp:
        x+=f(ui)
    v.g=x
    return v.g

#testy
print(fib_rek(10))
print(fib_rek(30))
print(fib_dyn(10))
print(fib_dyn(30))
A=[2,1,4,3,1,5,2,7,8,3]
ind,P=lis(A)
ps(A,P,ind)
print()
A=[1,3,5,2,4,5,3,4,6,3,5,1,3,4,6]
ind,P=lis(A)
ps(A,P,ind)
print()
a=Employee(50)
b=Employee(10)
c=Employee(20)
d=Employee(1)
e=Employee(18)
z=Employee(7)
x=Employee(12)
h=Employee(18)
i=Employee(5)
j=Employee(1)
k=Employee(2)
l=Employee(25)
m=Employee(36)
n=Employee(42)
o=Employee(100)
p=Employee(100)
r=Employee(1)
s=Employee(1)
t=Employee(1)
a.emp=[b,c,d]
b.emp=[e,z]
c.emp=[x,h]
d.emp=[i,j,k]
e.emp=[l,m,n]
x.emp=[o,p]
j.emp=[r,s]
k.emp=[t]
print(f(a))
a=Employee(25)
b=Employee(60)
c=Employee(70)
d=Employee(12)
e=Employee(13)
z=Employee(100)
x=Employee(100)
a.emp=[b,c]
b.emp=[d,e]
c.emp=[z,x]
print(f(a))
