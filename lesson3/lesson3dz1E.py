#print("{}. яблоко.\n".format(1),"{}. банан.\n".format(2),"{}. киви.\n".format(3),"{}. арбуз.\n".format(4))
list1 = ["яблоко", "банан", "киви", "арбуз"]
x = 0
for i in list1:
    if len(i) > x:
        x = len(i)
for i in range(len(list1)):
    print(("{0}. {1:>" + str(x) + "}").format(i + 1, list1[i]))
print()