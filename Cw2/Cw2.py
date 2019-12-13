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

def perceptron_learning(c):
    
    w = [1] * 26
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
            
    return t+1, w

print(perceptron_learning(1))
print(perceptron_learning(0.1))
print(perceptron_learning(0.01))
