from random import randint
n = int(input("Введите длинну списка: "))
list1 = [randint(-100, 100) for i in range(n)]
print('Случайный список:', list1)