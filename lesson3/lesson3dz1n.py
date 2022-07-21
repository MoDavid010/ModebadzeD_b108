from math import sqrt, modf
from random import randint
list1 = [randint(-10, 100) for i in range(10)]
list2 = []

for q in list1:
    if q >= 0:
        y = sqrt(q)
        x = modf(y)
        if y == x[1]:
            list2.append(int(y))

print('Исходный список: ', list1, '; Новый список: ', list2)