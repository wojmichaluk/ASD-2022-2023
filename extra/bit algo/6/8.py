#zadanie 8
def longest_palindrom(S):
    n=len(S)
    F=[[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i]=True
        if i<n-1 and S[i]==S[i+1]:
            F[i][i+1]=True
    for i in range(1,n-1):
        j=1
        mod=0
        if F[i][i+1]:
            mod=1
        while i-j>=0 and i+j+mod<n:
            if S[i-j]!=S[i+j+mod]:
                break
            F[i-j][i+j+mod]=True
            j+=1   
    longest=0
    indexes=(0,0)
    for i in range(n):
        for j in range(n-1,i-1,-1):
            if F[i][j]: break
        curr=j-i+1
        if curr>longest:
            longest=curr
            indexes=(i,j)
    return S[indexes[0]:indexes[1]+1]

#testy
S="kokon"
print(longest_palindrom(S))
S="napichcipaninapichcipan"
print(longest_palindrom(S))
S="abcdefghh"
print(longest_palindrom(S))
S="panna"
print(longest_palindrom(S))
