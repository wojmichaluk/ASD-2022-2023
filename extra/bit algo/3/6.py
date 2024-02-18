def SortTab(T,P):
    m=len(P)
    mi=P[0][0]
    ma=P[0][1]
    for i in range(1,m):
        mi=min(mi,P[i][0])
        ma=max(ma,P[i][1])
    n=len(T)
    A=[[] for _ in range(n+1)]
    for i in range(n):
        A[int(n*(T[i]-mi)/(ma-mi))].append(T[i])
    k=0
    for i in range(n+1):
        MergeSort(A[i])
        for j in range(len(A[i])):
            T[k]=A[i][j]
            k+=1

def MergeSort(A):
    n=len(A)
    if n>1:
        i=n//2
        L=A[:i]
        R=A[i:]
        MergeSort(L)
        MergeSort(R)
        j=k=0
        while j<i and k<n-i:
            if L[j]<=R[k]:
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

#testy
P=[(1,5,0.75),(4,8,0.25)]
T=[6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
SortTab(T,P)
print(T)
