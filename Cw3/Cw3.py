# Cw. 3
# Python

import numpy as np

z0 = np.array([0,0,0,0,0,
               0,1,1,1,0,
               0,1,0,1,0,
               0,1,1,1,0,
               0,0,0,0,0])

z1 = np.array([0,0,0,0,0,
               0,1,1,0,0,
               0,0,1,0,0,
               0,0,1,0,0,
               0,0,0,0,0])

z0[z0==0] = -1
z1[z1==0] = -1

W = np.zeros((25,25))

for i in range(25):
    for j in range(25):
        W[i][j] = (z0[i]*z0[j] + z1[i]*z1[j])/25

def associatron(u):
    u[u==0] = -1
    
    u = u.dot(W)

    u[u>=0] = 1
    u[u<0] = 0

    for i in range(5):
        for j in range(5):
            if u[i*5+j] == 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print("\n")
    print("----------------------")

associatron(np.array([0,0,0,0,0,
                      0,1,1,1,0,
                      0,1,0,1,0,
                      0,1,1,1,0,
                      0,0,0,0,0]))
associatron(np.array([0,0,0,0,0,
                      0,1,1,0,0,
                      0,0,1,0,0,
                      0,0,1,0,0,
                      0,0,0,0,0]))
associatron(np.array([0,1,1,1,0,
                      0,1,0,1,0,
                      0,1,0,1,0,
                      0,1,1,1,0,
                      0,0,0,0,0]))
associatron(np.array([0,0,1,0,0,
                      0,0,1,0,0,
                      0,0,1,0,0,
                      0,0,1,0,0,
                      0,0,1,0,0]))
