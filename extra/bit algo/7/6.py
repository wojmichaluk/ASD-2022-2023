#zadanie 6
def dict(word): #dana funkcja, O(1)
    return word in word_set

def can_be_words(string):
    n=len(string)
    DP=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            if dict(string[i:j+1]): DP[i][j]=1
            else: DP[i][j]=0
    Stack=[(0,[])]
    while Stack:
        pos,words=Stack.pop()
        if pos==n: return True,words
        i=pos
        while i<n:
            if DP[pos][i]: Stack.append((i+1,words+[string[pos:i+1]]))
            i+=1
    return False

#testy
word_set={"ala","ma","kota","i","nie","psa",
"lama","kot","mak","map","ta","lam"}
print("alamakota")
print(can_be_words("alamakota"))
print("alamakotainiemapsa")
print(can_be_words("alamakotainiemapsa"))
print("kotpsaalamani")
print(can_be_words("kotpsaalamani"))
