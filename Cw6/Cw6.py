# Cw. 6
# Python

import random
import math

# constants
C = 0.8
epsilon = 0.00001
beta = 1.0

def f(x):
    return 1/(1 + math.exp(-beta * x))

# Heaviside jump
def f_1(x):
    return 1 * (x > 0)

# initial condition
W = [[random.random() - 0.5 for _ in range(25)] for _ in range(16)]
Wp = [[random.random() - 0.5 for _ in range(25)] for _ in range(16)]
b = [random.random() - 0.5 for _ in range(25)]
bp = [random.random() - 0.5 for _ in range(25)]

# input
x1 = [0,0,0,0,0,
      0,1,1,0,0,
      0,0,1,0,0,
      0,0,1,0,0,
      0,0,1,0,0]

x2 = [0,0,1,1,0,
      0,0,0,1,0,
      0,0,0,1,0,
      0,0,0,0,0,
      0,0,0,0,0]

x3 = [0,0,0,0,0,
      1,1,0,0,0,
      0,1,0,0,0,
      0,1,0,0,0,
      0,1,0,0,0]

x = [x1, x2, x3]

# enkoder y
y = [[0 for a in range(16)] for _ in range(3)]

def enkoder(a):
    for alpha in range(3):
        for i in range(16):
            sum = 0
            for j in range(25):
                a[alpha][i] += W[i][j] * x[alpha][j] + b[i]
    return a

y = enkoder(y)

# dekoder xp
xp = [[0 for _ in range(25)] for a in range(3)]

def dekoder(a):
    for alpha in range(3):
        for k in range(25):
            sum = 0
            for i in range(16):
                a[alpha][i] += Wp[k][i] * y[alpha][i] + bp[k]
    return a

xp = dekoder(xp)

# pochodne:
DE_wp = []

DE_bp = []

DE_w = []

DE_b = []

# pochodna f
def Df(x):
    return beta * (1 - x)

# cel do zminimalizowania
E = [[0 for _ in range(25)] for _ in range(3)]

# zminimalizuj E metod¹ gradientu i wyznacz W oraz Wp:
for alpha in range(3):
    for k in range(25):
        E[alpha][k] = ((xp[alpha][k] - x[alpha][k])**2)/2


