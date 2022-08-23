a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3nd number: '))
d = b ** 2 - 4 * a * c
import math

if d < 0:
    print("not roots")
elif d == 0:
    x = - b / 2 * a
    print(x)
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(x1)
    print(x2)
