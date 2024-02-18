def chaos_index ( T ):
    n=len(T)
    for i in range(n):
        T[i]=(T[i],i)
    MergeSort(T)
    max_diff=T[0][1]
    for i in range(1,n):
        if abs(T[i][1]-i)>max_diff:
            max_diff=abs(T[i][1]-i)
    return max_diff

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
            if L[j][0]<=R[k][0]:
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
T=[0,2,1.1,2]
print(chaos_index(T))
T=[6,5,3,2,8,10,9]
print(chaos_index(T))
