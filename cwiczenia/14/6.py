#Jest m dzieci, każde ma n klocków różnej wysokości.
#Jedno dziecko zostało, kiedy reszta poszła na obiad
#i może podebrać (wymienić) kilka klocków od innych
#dzieci tak, żeby jego wieża była najwyższa. Szukamy
#minimalnej liczby klocków do zabrania.

from random import randint
from queue import PriorityQueue

#zadanie 6
def towers(pieces,child):
    m=len(pieces)
    n=len(pieces[0])
    sums=[sum(pieces[i]) for i in range(m)]
    queues=[PriorityQueue() for _ in range(m)]
    for i in range(m):
        if i==child:
            for j in range(n):
                queues[i].put(pieces[i][j])
        else:
            for j in range(n):
                queues[i].put(-pieces[i][j])
    pieces_taken=0
    print("index of child who takes:",child)
    print("before:",sums)
    while not solo_max(sums,child):
        pieces_taken+=1
        most_worthwhile(queues,sums,child)
    print("after:",sums)
    return pieces_taken

def solo_max(sums,child):
    return sums[child]>max_except(sums,child)

def max_except(sums,child):
    m=len(sums)
    max_sum=-float('inf')
    for i in range(m):
        if i!=child and sums[i]>max_sum:
            max_sum=sums[i]
    return max_sum

def most_worthwhile(queues,sums,child):
    m=len(queues)
    sums_dif=[float('inf') for _ in range(m)]
    given=queues[child].get()
    for i in range(m):
        taken=-1*queues[i].get()
        sums[i]+=given-taken
        sums[child]+=taken-given
        sums_dif[i]=max_except(sums,child)-sums[child]
        sums[i]+=taken-given
        sums[child]+=given-taken
        queues[i].put(-taken)
    sums_dif[child]=float('inf')
    min_sum=sums_dif[0]
    min_ind=0
    for i in range(1,m):
        if sums_dif[i]<min_sum:
            min_sum=sums_dif[i]
            min_ind=i
    taken=-1*queues[min_ind].get()
    queues[child].put(taken)
    queues[min_ind].put(-given)
    sums[min_ind]+=given-taken
    sums[child]+=taken-given

#testy
pieces=[[3,1,5,6],[2,5,4,3],[1,7,6,5]]
print("pieces exchanged:",towers(pieces,0),'\n')
print("pieces exchanged:",towers(pieces,1),'\n')
print("pieces exchanged:",towers(pieces,2),'\n')
for j in range(10**0):
    pieces=[[randint(1,100) for _ in range(10)] for _ in range(10)]
    for i in range(10):
        print("pieces exchanged:",towers(pieces,i),'\n')
