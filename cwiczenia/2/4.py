#Mamy dany zbiór przedziałów. Znaleźć przedział, 
#który zawiera najwięcej innych przedziałów.

from random import randint

#zadanie 4    
def merge_sort(A,tpl_nr):
    n=len(A)
    if n>1:
        i=n//2
        L=A[:i]
        R=A[i:]
        merge_sort(L,tpl_nr)
        merge_sort(R,tpl_nr)
        j=k=0
        while j<i and k<n-i:
            if L[j][tpl_nr]==R[k][tpl_nr]:
                if L[j][1-tpl_nr]>=R[k][1-tpl_nr]:
                    A[j+k]=L[j]
                    j+=1
                else:
                    A[j+k]=R[k]
                    k+=1
            elif L[j][tpl_nr]<R[k][tpl_nr]:
                A[j+k]=L[j]
                j+=1
            else:
                A[j+k]=R[k]
                k+=1
        while j<i:
            A[j+k]=L[j]
            j+=1
        while k<n-i:
            A[j+k]=R[k]
            k+=1

def range_positions(A):
    merge_sort(A,0)
    for i in range(len(A)):
        A[i]+=(i,)
    merge_sort(A,1)
    for i in range(len(A)):
        A[i]+=(i,)
    max_range=A[0]
    max_incl=A[0][3]-A[0][2]
    for element in A[1:]:
        if max_incl<element[3]-element[2]:
            max_range=element
            max_incl=element[3]-element[2]
    return max_range[0],max_range[1]

#testy
T=[(randint(1,10),randint(11,20)) for _ in range(10)]
print(*T)
print(range_positions(T))
for i in range(len(T)):
    print("(",T[i][0],",",T[i][1],") ",T[i][3]-T[i][2],sep='')
