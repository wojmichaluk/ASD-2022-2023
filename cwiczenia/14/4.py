#Zachłan do problemu wydawania reszty - muszą
#być spełnione warunki: 1) 1 należy do C; 2) dla
#każdego i, c_i >= 2 * c_i-1.
#
#Ładowanie przyczepy - pojemność K kilogramów,
#zbiór ładunków o wagach w1,w2,...,wn. Wagi są
#potęgami 2. Chcemy wybrać ładunki tak, żeby
#maksymalnie załadować przyczepę i jednocześnie
#użyć jak najmniej ładunków. Pomysł: sortujemy
#ładunki po wagach i problem sprowadza się do
#"wydania reszty".

#zadanie 4
def min_cargos(W,K):
    W.sort()
    m=W[0]
    to_spare=K%m
    left=K
    cargos=[]
    curr_index=len(W)-1
    while left>to_spare and curr_index>=0:
        while W[curr_index]>left:
            curr_index-=1
        left-=W[curr_index]
        cargos.append(W[curr_index])
        curr_index-=1
    return cargos,len(cargos),not left

#testy
W=[2,16,4,8,8,16,6,2,64]
print(min_cargos(W,43))
W=[2,16,4,128,16,8,1,64,32,128,64]
print(min_cargos(W,245))
W=[16,1,32,1,1,1,128,64,256,2,2,1]
print(min_cargos(W,245))
