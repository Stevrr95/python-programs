from math import *

i = 2
num = float(input("Enter a number: "))

while (i < num):
    result = num % i
    if result == 0:
        print(num,"is not a Prime number")
        break
    i += 1
if result != 0:
    print(num,"is a Prime number")
