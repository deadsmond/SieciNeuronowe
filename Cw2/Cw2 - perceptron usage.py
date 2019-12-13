# Cw. 2
# Python

u1 = [0,0,0,0,0,
      0,1,1,0,0,
      0,0,1,0,0,
      0,0,1,0,0,
      0,0,1,0,0,1]

u2 = [0,0,1,1,0,
      0,0,0,1,0,
      0,0,0,1,0,
      0,0,0,0,0,
      0,0,0,0,0,1]

u3 = [0,0,0,0,0,
      1,1,0,0,0,
      0,1,0,0,0,
      0,1,0,0,0,
      0,1,0,0,0,1]

u4 = [0,0,0,0,0,
      0,1,1,1,0,
      0,1,0,1,0,
      0,1,1,1,0,
      0,0,0,0,0,1]

u5 = [0,0,0,0,0,
      0,0,0,0,0,
      1,1,1,0,0,
      1,0,1,0,0,
      1,1,1,0,0,1]

u = [u1, u2, u3, u4, u5]
global w
w = [1] * 26

def perceptron_learning(c):
    
    t = 0
    counter = 0

    while counter != 5:
        
        z = 1 * ( t%5 + 1 <= 3 )
        
        y = 1 * ( sum( u[t%5][i]*w[i] for i in range (len (u[t%5]))) >= 0 )

        for i in range (len (u[t%5])):
            w[i] = w[i] + c * (z - y) * u[t%5][i]
        
        t = t + 1        
        if z == y:
            counter = counter + 1
        else:
            counter = 0

def perceptron_usage(ub):
    e = sum( ub[i]*w[i] for i in range (len (ub)))
    return 1 * (e > 0)

#perceptron_learning(1)
#perceptron_learning(0.1)
perceptron_learning(0.01)

print(perceptron_usage([0,0,1,0,0,
                        0,0,1,0,0,
                        1,1,1,0,0,
                        1,0,1,0,0,
                        1,1,1,0,0,1]))


