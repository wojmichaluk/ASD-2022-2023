#Mamy zbiór zadań T={t1,t2,...,tn}. Każde
#zadanie ti ma dodatkowo deadline d(ti) oraz
#zysk g(ti) [liczby naturalne]. Każde zadanie
#zabiera jednostkę czasu, zaczynamy w chwili 0.
#Uwaga - zysk liczymy tylko wtedy, gdy zdążymy 
#przed terminem! Szukamy doboru zadań, żeby zysk
#był maksymalny. Pomysł: idziemy od końca
#i wybieramy najbardziej opłacalne zadanie. 
#Sortujemy malejąco po deadline, można np.
#wykorzystać max_heap.

from queue import PriorityQueue

#zadanie 3
def tasks(G,D):
    n=len(G)
    q=PriorityQueue()
    for i in range(n):
        q.put((-D[i],-G[i]))
    done_tasks=0
    curr_gains=0
    deadline=max(D)
    while not q.empty() and deadline:
        d,g=q.get()
        d*=-1
        temp=[]
        while d>deadline:
            temp.append(-g)
            d,g=q.get()
            d*=-1
        if d<deadline:
            q.put((-d,g))
            if temp:
                val,ind=find_max(temp)
                curr_gains+=val
                for i in range(len(temp)):
                    if i!=ind:
                        q.put((-deadline,-temp[i]))
                done_tasks+=1
        else:
            val=-float('inf')
            if temp: val,ind=find_max(temp)
            if -g>val:
                curr_gains-=g
                for i in range(len(temp)):
                    q.put((-deadline,-temp[i]))
            else:
                q.put((-d,g))
                curr_gains+=val
                for i in range(len(temp)):
                    if i!=ind:
                        q.put((-deadline,-temp[i]))
            done_tasks+=1
        deadline-=1
    return done_tasks,curr_gains

def find_max(T):
    max_val=T[0]
    max_ind=0
    for i in range(1,len(T)):
        if T[i]>max_val:
            max_val=T[i]
            max_ind=i
    return max_val,max_ind

#testy
gains=[10,6,7,5,3,1]
deadlines=[4,2,3,4,2,1]
print(tasks(gains,deadlines))
gains=[8,6,12,5,9,4]
deadlines=[8,5,4,4,6,2]
print(tasks(gains,deadlines))
gains=[10,4,6,7,11,5,3,8,1,2]
deadlines=[1,2,1,2,1,2,1,2,1,2]
print(tasks(gains,deadlines))
gains=[10,4,6,7,6]
deadlines=[1,1,1,1,5]
print(tasks(gains,deadlines))
