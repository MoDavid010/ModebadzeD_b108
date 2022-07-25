list1 = ["банан", "апельсин", "яюлоко", "мандарин", "арбуз"]
list2 = ["яюлоко", "мандарин", "груша", "киви", "арбуз"]
new_list = []
for i in list1:
    if i in list2:
        new_list.append(i)

print(list1)
print(list2)
print(new_list)