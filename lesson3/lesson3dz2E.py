list1 = [1, 2, 6, 9, 5, "Alex"]
list2 = [8, 5, 'Alex', 2, 9]
x = []
for i in list1:
    if i not in list2:
        x.append(i)
list1 = x
print(list1, list2)
