from math import * 

N = 64
a = 7
b = a*a - N

carre = []
for i in range (50):
    carre.append(i*i)


def fermat(N):
    a = ceil(sqrt(N))
    b = a*a - N
    while b not in carre:
        a += 1
        b = a*a - N

    return a, b
   



print(fermat(65))





