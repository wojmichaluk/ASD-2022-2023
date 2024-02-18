#Dane są dwa napisy. Proszę zaimplementować 
#funkcję sprawdzającą, czy są anagramami.

#zadanie 4
def anagram (w1,w2):
    n1=len(w1)
    n2=len(w2)
    if n1!=n2: return False
    T=[0]*(ord('z')-ord('a')+1)
    for ch in w1:
        T[ord(ch)-ord('a')]+=1
    for ch in w2:
        T[ord(ch)-ord('a')]-=1
        if T[ord(ch)-ord('a')]<0: return False
    return True

#testy
print(anagram("kott","ktot"))
print(anagram("kobjksbfkjsbfkj","kbjsfkjskobbfkj"))
print(anagram("kottdhdgjgt","kottydhdgjgt"))
print(anagram("jfsgkjfgskgak","jgfkjsfkgagks"))
print(anagram("kottdhjdfdhd","kotdhjdfduhd"))
