from queue import PriorityQueue

#zadanie 3
def timetable(times,m):
    n=len(times)
    q=PriorityQueue()
    for i in range(n):
        q.put((times[i][0],1))
        q.put((times[i][1],-1))
    cnt=0
    while not q.empty():
        t,l=q.get()
        cnt+=l
        if cnt>m: return False
    return True

#testy
times=[(1,5),(1,4),(2,8),(2,6),(3,5),(4,7),(5,8),(5,10)]
print(timetable(times,4))
print(timetable(times,6))
times=[(1,4),(1,10),(2,8),(2,6),(3,6),(3,7),(4,5),
(4,7),(5,12),(5,10),(6,8),(6,10),(7,10),(7,11),(8,13)]
print(timetable(times,8))
print(timetable(times,10))
