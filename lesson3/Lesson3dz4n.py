from random import randint
list1 = [randint(0, 20) for i in range(10)]
print('Исходный список: ', list1)
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print('Неповторяющиеся элементы исходного списка: ', list2)

list3 = []
for i in list1:
    if list1.count(i) == 1:
        list3.append(i)
print('Элементы исходного списка, которые не имеют повторений: ', list3)