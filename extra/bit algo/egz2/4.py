from egz2btesty import runtests

#zadanie 4
def magic( C ):
    n=len(C)
    DP=[-1 for _ in range(n)]
    DP[0]=0
    for i in range(n-1):
        if DP[i]>=0:
            gold,c1,c2,c3=C[i]
            if c1[1]!=-1:
                taken=gold-c1[0]
                if taken<=10 and DP[i]+taken>=0:
                    DP[c1[1]]=max(DP[c1[1]],DP[i]+taken)
            if c2[1]!=-1:
                taken=gold-c2[0]
                if taken<=10 and DP[i]+taken>=0:
                    DP[c2[1]]=max(DP[c2[1]],DP[i]+taken)
            if c3[1]!=-1:
                taken=gold-c3[0]
                if taken<=10 and DP[i]+taken>=0:
                    DP[c3[1]]=max(DP[c3[1]],DP[i]+taken)
    return DP[n-1]

#testy
runtests( magic, all_tests = True )
