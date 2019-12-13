# Cw. 5
# Python

import math
import copy

# space of all possible states
u = [[0, 0, 1],
     [1, 0, 1],
     [0, 1, 1],
     [1, 1, 1]]

x = [[0.0, 0.0, 1.0],
     [0.0, 0.0, 1.0],
     [0.0, 0.0, 1.0],
     [0.0, 0.0, 1.0]]

w = [[0.0, 1.0, 2.0],
     [0.0, 1.0, 2.0]]

w_new = [[0.0, 0.0, 0.0],
         [0.0, 0.0, 0.0]]

s = [0.0, 1.0, 2.0]
s_new = [0.0, 0.0, 0.0]

y = [0.0, 0.0, 0.0, 0.0]
z = [0.0, 1.0, 1.0, 0.0]

# constants
c = 0.1
epsilon = 0.000001
beta = 1.0

# reduction
def f(_):
    try:
        return 1 / (1 + math.exp(- beta * _))
    except OverflowError:
        return float('inf')

def Df(_):
    t = f(_)
    return beta * t * (1 - t)

# pochodne
DE_s = [0, 0, 0]

DE_w = [[0, 0, 0],
        [0, 0, 0]]

def calculate_DE_s(i_):
    DE_s[i_] = 0
    for p in [0, 1, 2, 3]:
        DE_s[i_] = DE_s[i_] + (y[p] - z[p]) * Df(s[0] * x[p][0] + s[1] * x[p][1] + s[2] * x[p][2]) * x[p][i_]

def calculate_DE_w(i_, j_):
    DE_w[i_][j_] = 0
    for p in [0, 1, 2, 3]:
        DE_w[i_][j_] = DE_w[i_][j_] + (y[p] - z[p]) * Df(s[0] * x[p][0] + s[1] * x[p][1] + s[2] * x[p][2]) * s[i_] * Df(w[i_][0] * u[p][0] + \
            w[i_][1] * u[p][1] + w[i_][2] * u[p][2]) * u[p][j_]

def calculate_x():
    for p in [0, 1, 2, 3]:
        for i_ in [0, 1]:
            # x[p][2] = 1
            x[p][i_] = f(w[i_][0] * u[p][i_] + w[i_][1] * u[p][i_] + w[i_][2] * u[p][i_])

def calculate_y():
    for p in [0, 1, 2, 3]:
        y[p] = f(s[0] * x[p][0] + s[1] * x[p][1] + s[2] * x[p][2])

# gradient
while True:
    max_ = -999

    # set new x
    calculate_x()
    # set new y
    calculate_y()

    # new s
    for i in [0, 1, 2]:
        # set new s
        calculate_DE_s(i)
        s_new[i] = s[i] - c * DE_s[i]
        # set max
        if abs(s_new[i] - s[i]) > max_:
            max_ = abs(s_new[i] - s[i])

    # new w
    for i in [0, 1]:
        # for j in [0, 1, 2]:
        for j in range(2):
            # set new w
            calculate_DE_w(i, j)
            w_new[i][j] = w[i][j] - c * DE_w[i][j]
            # set max
            if abs(w_new[i][j] - w[i][j]) > max_:
                max_ = abs(w_new[i][j] - w[i][j])

    if max_ < epsilon:
        break

    s = copy.deepcopy(s_new)
    w = copy.deepcopy(w_new)

# print results
print(w)
print(s)
for _ in range(4):
    print(y[_])
