from math import *

x1 = 0
n = 0
y1 = 1

while True:
    x = float(input("x: "))
    if x == -1:
        break
    else:
        AR = x
        GM = sqrt(y1 * x)
        AR2 = AR + x1
        x1 = AR2
        y1 = GM ** 2
        n += 1
AR2 /= n
print("Arithmetic Mean is",AR2)
print("Geometric Mean is",GM)
