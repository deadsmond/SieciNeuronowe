# Cw. 1
# Python

def neuron(u, type):
    if type == "NOT":
        w = [-0.5, 0.5]
    elif type == "AND":
        w = [0.3, 0.3, -0.5]
    elif type == "NAND":
        w = [-0.3, -0.3, 0.5]
    elif type == "OR":
        w = [0.2, 0.2, -0.1]

    e = sum( u[i]*w[i] for i in range (len (u)))
    return 1 * (e > 0) 

print(neuron([0,1],"NOT"))
print(neuron([1,1],"NOT"))
print(neuron([0,1,1],"AND"))
print(neuron([1,1,1],"AND"))
print(neuron([0,1,1],"NAND"))
print(neuron([1,1,1],"NAND"))
print(neuron([0,1,1],"OR"))
print(neuron([1,1,1],"OR"))
print(neuron([0,0,1],"OR"))
