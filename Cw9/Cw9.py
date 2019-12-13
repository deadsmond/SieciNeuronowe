# Cw. 9
# Python

import random
import math

# zaszyfrowana informacja o kosztach podróży między punktami a i b - ver. 1
def d_1(a, b):
    if [a,b] == [1, 10] or [a,b] == [10, 1]:
        return 1
    return abs(a-b)

# zaszyfrowana informacja o kosztach podróży między punktami a i b - ver. 2
def d_2(a, b):
    if [a,b] == [1, 2] or [a,b] == [9, 10]:
        return 1
    elif a < b:
        return a**3 + b**3 - a**2 * b - a * b**2 + 4*(a**2 - b**2 + a + b) + 1
    elif a == b:
        return 0
    return d_2(b, a)

# wyznaczenie różnicy energii
def E(S, d):
    e = 0
    for i in range(len(S)-1, 0, -1):
        e = e + d(S[i], S[i-1])
    return e

# rozwiązanie problemu komiwojażera
def TSP(T_0, L, M, d):

    T = T_0
    t = 0

    # random beginning state
    S = list(range(1, 11))
    random.shuffle(S)
    S_p = S[:]

    # dopóki nie spełniono warunku zatrzymania
    accepted = 0
    all_count = 0
    while accepted < L:
        
        # dopóki nie osiągnięto stanu równowagi - REPAIR
        while all_count < M:
            
            # nowe sąsiednie rozwiązanie generowane losowo
            all_count = all_count + 1
            
            i = random.randint(0, 9)
            j = random.randint(0, 9)
            while i == j:
                i = random.randint(0, 9)
                j = random.randint(0, 9)
            S_p[i], S_p[j] = S_p[j], S_p[i]
            
            # wyznaczenie różnicy energii
            E_p = E(S_p, d) - E(S, d)
            
            # jeśli S_p jest akceptowany
            if E_p < 0 or random.random() < math.exp(-E_p/T):
                accepted = accepted + 1
                S = S_p
                
        # aktualizacja T
        t = t + 1
        T = T_0 / (1 + math.log(t))

    return S, E(S, d)

# wywołanie algorytmu i uzyskanie odpowiedzi
print(TSP(100, 3, 10, d_1))
print(TSP(100, 3, 10, d_1))
print(TSP(100, 3, 10, d_1))
print(TSP(100, 3, 10, d_1))
print(TSP(100, 3, 10, d_1))
print(TSP(100, 3, 10, d_1))
print(TSP(100, 3, 10, d_1))
print(TSP(100, 3, 10, d_1))
print(TSP(100, 3, 10, d_1))
print(TSP(5, 5, 150, d_2))
print(TSP(5, 5, 150, d_2))
print(TSP(5, 5, 150, d_2))
print(TSP(5, 5, 150, d_2))
print(TSP(5, 5, 150, d_2))
print(TSP(5, 5, 150, d_2))
print(TSP(5, 5, 150, d_2))
print(TSP(5, 5, 150, d_2))
print(TSP(5, 5, 150, d_2))
print(TSP(5, 5, 150, d_2))
print(TSP(5, 5, 150, d_2))
print(TSP(5, 5, 150, d_2))

        
