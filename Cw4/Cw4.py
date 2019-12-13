# Cw. 4
# Python

import random

c = 0.01
E = 0.0000001

def pochodna_x (x, y, z):
    return 4*x - 2*y - 2

def pochodna_y (x, y, z):
    return 4*y - 2*x - 2*z

def pochodna_z (x, y, z):
    return 2*z - 2*y

def pochodna_x2 (x, y):
    return 12*x**3 + 12 * x**2 - 24 * x

def pochodna_y2 (x, y):
    return 24 * y - 24

# pierwsza funkcja
x_old, y_old, z_old = random.random(), random.random(), random.random()
# x_old, y_old, z_old = 2, 3, 4

max = 0
x_new, y_new, z_new = 0, 0, 0

while True:
    x_new = x_old - c*pochodna_x(x_old, y_old, z_old)
    y_new = y_old - c*pochodna_y(x_old, y_old, z_old)
    z_new = z_old - c*pochodna_z(x_old, y_old, z_old)

    max = 0
    if abs(x_new - x_old) > max:
        max = abs(x_new - x_old)
    if abs(y_new - y_old) > max:
        max = abs(y_new - y_old)
    if abs(z_new - z_old) > max:
        max = abs(z_new - z_old)
    if max < E:
        break

    x_old, y_old, z_old = x_new, y_new, z_new

print(x_new, y_new, z_new, 2*x_new**2 + 2*y_new**2 + z_new**2 - 2*x_new*y_new - 2*y_new*z_new - 2*x_new + 3)

# druga funkcja
x_old, y_old = random.random(), random.random()
# x_old, y_old = 2, 3

max = 0
x_new, y_new = 0, 0

while True:
    x_new = x_old - c*pochodna_x2(x_old, y_old)
    y_new = y_old - c*pochodna_y2(x_old, y_old)

    max = 0
    if abs(x_new - x_old) > max:
        max = abs(x_new - x_old)
    if abs(y_new - y_old) > max:
        max = abs(y_new - y_old)
    if max < E:
        break

    x_old, y_old = x_new, y_new

print(x_new, y_new, 3*x_new**4 + 4*x_new**3 - 12 *x_new**2 + 12*y_new**2 - 24*y_new)
