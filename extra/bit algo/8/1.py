#zadanie 1
def tank(s,d,F):
    n=len(s)
    stop_points=[0 for _ in range(n+2)]
    for i in range(1,n+1):
        stop_points[i]=s[i-1]
    stop_points[n+1]=F
    far=[]
    tanks=0
    pos=0
    while True:
        new_pos=find_furthest(stop_points,pos,d)
        if new_pos==pos: return None
        pos=new_pos
        if pos==n+1: break
        far.append(stop_points[pos])
        tanks+=1
    return tanks,far

def find_furthest(stops,pos,d):
    n=len(stops)
    last=pos
    for i in range(pos+1,n):
        if stops[i]>stops[pos]+d: break
        last=i
    return last
    
#testy
stations=[2,4,7]
print(tank(stations,4,9))
stations=[2,3,5,6,10,15]
print(tank(stations,8,19))
stations=[2,5,7,11,18,23,34,36]
print(tank(stations,10,39))
