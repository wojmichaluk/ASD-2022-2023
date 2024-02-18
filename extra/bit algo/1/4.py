class Count:
    def __init__(self,k,T):
        self.k=k
        self.T=T
        self.aux=[0]*(k+1)
        for elem in self.T:
            self.aux[elem]+=1
        for i in range(k):
            self.aux[i+1]+=self.aux[i]

    def count_num_in_range(self,a,b):
        if a>=1 and b<=self.k:
            return self.aux[b]-self.aux[a-1]

#testy
T=[0,7,5,3,8,4,7,4,2,8,1,6,10,9]
A=Count(10,T)
print(A.count_num_in_range(1,10))
print(A.count_num_in_range(3,6))
print(A.count_num_in_range(5,9))
