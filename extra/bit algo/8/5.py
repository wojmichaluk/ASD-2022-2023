#zadanie 5
def intervals(T,k):
    T.sort(key=lambda x: x[1])
    n=len(T)
    min_sol=[]
    min_diff=float('inf')
    for i in range(n-k+1):
        curr_sol,curr_diff=find_kset(T,i,k)
        if len(curr_sol)==k:
            if curr_diff<min_diff:
                min_sol=curr_sol
                min_diff=curr_diff
    if not min_sol: return False
    return min_sol,min_diff

def find_kset(T,i,k):
    curr_set=[T[i]]
    n=len(T)
    j=i+1
    while len(curr_set)<k and j<n:
        if T[j][0]>=curr_set[-1][1]:
            curr_set.append(T[j])
        j+=1
    diff=curr_set[-1][1]-curr_set[0][0]
    return curr_set,diff

#testy
T=[(1,5),(3,8),(2,6),(6,12),(7,13),(12,15),(4,9)]
print(intervals(T,3))
print(intervals(T,4))
T=[(1,2),(3,6),(2,4),(6,10),(7,10),(12,15),(4,8),
(2,5),(6,9),(10,12),(8,11),(5,9),(3,7),(15,20)]
print(intervals(T,4))
print(intervals(T,6))
