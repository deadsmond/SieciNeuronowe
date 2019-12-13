# Cw. 10
# Python

import random

def GCD(a, b):
    if a%b == 0:
        return b
    return GCD(b, a%b)

def factorian(N):
    t = N**2
    while True:
        # 1
        a = random.randint(1, N)

        # 2
        tGCD = GCD(N, a)
        if tGCD > 1:
            return tGCD
        
        # 3 - solve Discrete Log Problem with bruteforce
        r = 0

        while (a**r-1)%N == 0 and (a**r) < t:
            r = r + 1
            
        if r%2:
            
            # 4
            if GCD(N, a**(r/2)-1) > 1:
                return tGCD
            if GCD(N, a**(r/2)+1) > 1:
                return tGCD

# main loop
print(factorian(12))
print(factorian(15))
print(factorian(91))
print(factorian(143))
print(factorian(1859))
print(factorian(1737))
print(factorian(13843))
print(factorian(988027))
