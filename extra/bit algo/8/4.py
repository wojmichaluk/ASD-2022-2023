#zadanie 4
def covid(arr,k):
    n=len(arr)
    if k>=n:
        for i in range(n):
            if arr[i]: return [i],1
        return -1
    pos=k-1
    while not arr[pos]:
        if not pos: return -1
        pos-=1
    positions=[pos]
    machines=1
    while pos<n-k:
        new_pos=find_pos(pos,arr,k)
        if new_pos==pos: return -1
        pos=new_pos
        positions.append(pos)
        machines+=1
    return positions,machines

def find_pos(pos,arr,k):
    new_pos=min(pos+2*k-1,len(arr)-1)
    while not arr[new_pos]: new_pos-=1
    return new_pos

#testy
arr=[0,0,1,0,1,0,0,1,0,1,1,0,0,1,0]
print(covid(arr,4))
arr=[0,0,0,0,1,0,0,0,0,0,1,0,0,1,0]
print(covid(arr,4))
arr=[0,0,1,0,1,0,0,0,0,0,1,0,0,1,0]
print(covid(arr,4))
arr=[0,0,1]
print(covid(arr,3))
arr=[0,0,0]
print(covid(arr,3))
