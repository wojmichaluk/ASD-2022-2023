#zadanie 5
def longest_path_in_DAG(G,s):
    n=len(G)
    DP=[None for _ in range(n)]
    return rek(G,DP,s)

def rek(G,DP,s):
    if DP[s]!=None: return DP[s]
    longest=0
    for i in range (len(G[s])):
       if G[s][i]: longest=max(longest,G[s][i]+rek(G,DP, i))
    DP[s]=longest
    return longest

#testy
G=[[0,4,10],[0,0,3],[0,0,0]]
print(longest_path_in_DAG(G,0))
G=[[0,4,10],[0,0,7],[0,0,0]]
print(longest_path_in_DAG(G,0))
G=[[0,0,0,0,0,0],[5,0,0,0,0,0],[0,0,0,0,2,0],
[7,3,0,0,1,0],[0,11,0,0,0,6],[0,4,0,0,0,0]]
print(longest_path_in_DAG(G,3))
G=[[0,0,0,0,0,0],[5,0,0,0,0,0],[0,0,0,0,2,0],
[7,3,0,0,1,0],[0,8,0,0,0,6],[0,4,0,0,0,0]]
print(longest_path_in_DAG(G,3))
