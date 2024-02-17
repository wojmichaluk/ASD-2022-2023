#Wojciech Michaluk
#Algorytm szuka środka palindromu (korzystając z tego, że ma on
#nieparzystą długość). W tym celu przechodzi po indeksach, poczynając
#od drugiego elementu. Następnie, w zakresie danego wyrazu, sprawdza czy
#element jest środkiem palindromu - bada symetrię znaków względem tego
#elementu. Ograniczenie górne dla indeksu, który jest potencjalnym środkiem,
#wynika z długości dotychczasowo znalezionego najdłuższego palindromu.
#Szacuję rząd złożoności na O(n^2), ale usprawnione np. wspomnianym
#ograniczeniem górnym.

from zad1testy import runtests

def ceasar( s ):
    n=len(s)
    i=1
    longest=1
    while i<n-longest//2-1:
        current=1
        for j in range(1,i+1):
            if i+j>=n:
                break
            if not (s[i-j]==s[i+j]):
                break
            current+=2
        longest=max(longest,current)
        i+=1
    return longest
 
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
