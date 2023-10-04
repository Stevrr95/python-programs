from math import *

prev_integer = 0
n = 0

while True:
    integer = float(input("Enter an integer:"))
    if integer == 0:
        break
    _sum = integer + prev_integer
    prev_integer = _sum
    n += 1

_average = _sum / n
_average = int(_average)
_sum = int(_sum)

print("The sum of the numbers is:",_sum)
print("The average of the numbers is:",_average)
