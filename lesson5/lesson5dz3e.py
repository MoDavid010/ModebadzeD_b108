original_list = [5, 8, 15,  36, 9, -10, 23]
new_list = []

for i in original_list:
    if i % 3 == 0 and i > 0 and i % 4 != 0:
        new_list.append(i)
print(new_list)
