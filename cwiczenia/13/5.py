#Dwuwymiarowy problem plecakowy - wersja
#dyskretna, mamy wartość, wagę i wysokość
#przedmiotu. W - maksymalna waga, H - maks.
#wysokość. Pomysł: f(i,w,h) = max(f(i-1,w,h),
#f(i-1,w-w_i,h-h_i) + v_i); dla i = 0: v_0,
#jeżeli w_0<=w i h_0<=h, 0 w przeciwnym razie.

from random import randint

#zadanie 5
def knapsack2D_rek(W,H,P,i,w,h): #rekurencyjnie
    if i==0:
        if W[0]<=w and H[0]<=h: return P[0]
        return 0
    a=b=0
    a=knapsack2D_rek(W,H,P,i-1,w,h)
    if W[i]<=w and H[i]<=h: b=knapsack2D_rek(W,H,P,i-1,w-W[i],h-H[i])+P[i]
    return max(a,b)

def knapsack2D(weights,heights,P,W,H): #dynamicznie
    n=len(weights)
    F=[[[0 for _ in range(H+1)] for _ in range(W+1)] for _ in range(n)]
    for w in range(weights[0],W+1):
        for h in range(heights[0],H+1):
            F[0][w][h]=P[0]
    for w in range(W+1):
        for h in range(H+1):
            for i in range(1,n):
                F[i][w][h]=F[i-1][w][h]
                if w-weights[i]>=0 and h-heights[i]>=0 and F[i-1][w-weights[i]][h-heights[i]]+P[i]>F[i][w][h]:
                    F[i][w][h]=F[i-1][w-weights[i]][h-heights[i]]+P[i]
    return F[n-1][W][H]

#testy
P=[1,3,2]
weights=[4,7,6]
heights=[5,6,3]
print(knapsack2D_rek(weights,heights,P,len(P)-1,12,8))
print(knapsack2D(weights,heights,P,12,8))
P=[10,13,22,8,21,15]
weights=[2,3,6,4,5,7]
heights=[5,7,6,2,3,4]
print(knapsack2D_rek(weights,heights,P,len(P)-1,20,15))
print(knapsack2D(weights,heights,P,20,15))
P=[randint(5,40) for _ in range(15)]
weights=[randint(10,20) for _ in range(15)]
heights=[randint(10,20) for _ in range(15)]
print(knapsack2D_rek(weights,heights,P,len(P)-1,100,100))
print(knapsack2D(weights,heights,P,100,100))
