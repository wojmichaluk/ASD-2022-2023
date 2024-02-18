#zadanie 6
def bin_strings(n):
    F=[1 for _ in range(n+2)]
    for i in range(2,n+2):
        F[i]=F[i-1]+F[i-2]
    return F[n+1]

#testy
print(bin_strings(0))
print(bin_strings(5))
print(bin_strings(7))
print(bin_strings(1))
print(bin_strings(4))
