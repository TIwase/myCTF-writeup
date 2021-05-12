# -*- coding: utf-8 -*-
from math import gcd

n = 851
seed = 2  # seedは通常2か3, うまく分解できなかったときに動かす
B = 100000 # B-smoothと仮定する 通常100000まで

# a = seed
G = 1
cnt = 0
M = 1

while(G<=1):
    M = M + 1
    # print("M: ", M)
    if M >= B:
        break
    if M % B == 0:
        print("M=" + str(M))
    # print("a = a ^ M mod n = ", a, "^", M, " mod ", n)
    a = pow(a, M, n)
    # print("= ", a)
    G = gcd(a-1, n)
    # print("G = gcd( a-1, n ) = ", "gcd(" , a-1, ", ", n, ") = ", G)
if G > 1 and G < n:
    print("factor is " + str(G) + ", M = " + str(M))
else:
    print("try new seed")

print("p: " + str(G))
print("q: " + str(n//G))
