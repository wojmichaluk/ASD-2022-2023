#zadanie 1
def tanagram(x,y,t):
    if len(x)!=len(y): return False
    n=len(x)
    if t>n-1: t=n-1
    cnt=[0 for _ in range(ord('z')-ord('a')+1)]
    for i in range(t+1):
        cnt[ord(x[i])-97]+=1
    for i in range(n-t-1):
        if not cnt[ord(y[i])-97]: return False
        cnt[ord(y[i])-97]-=1
        cnt[ord(x[t+1+i])-97]+=1
        if i>t and cnt[ord(x[i-t-1])-97]:
            cnt[ord(x[i-t-1])-97]-=1
    for i in range(t+1):
        if not cnt[ord(y[n-t-1+i])-97]: return False
        cnt[ord(y[n-t-1+i])-97]-=1
    return True

#testy
print(tanagram("kotomysz","tokmysoz",3))
print(tanagram("kotomysz","tokmysoz",2))
print(tanagram("tosamo","tosamo",0))
print(tanagram("michaszpies","szpimhcisae",4))
print(tanagram("testtyt","testsos",3))
print(tanagram("testtyyyt","testytyty",4))
