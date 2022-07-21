x = int(input('Ведите число: '))
y = 0
while x > 0:
    c = x % 10
    if c >= y:
        y = c
    x = x // 10
print(y)