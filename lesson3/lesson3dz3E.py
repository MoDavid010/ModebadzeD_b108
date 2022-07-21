list1 = [5, 8, 7, 31, 44, 85, 3, 1, 10, 55, 71, 9]
x = []
print(list1)
for i in list1:
    if i % 2 == 0: # если при длении на 2 останот i = 0
        x.append(int(i / 4)) # добовляем новый элемент в список
    else:
        x.append(i * 2)
print(x)
