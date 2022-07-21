def fibonacci(n, m):

    a = 1
    b = 2
    f = [1, ]

    for i in range(m):
        a = b
        b = a + b
        f.append(a)

    return f[n - 1:m]

print('fibonacci(1, 6): ', fibonacci(1, 6))

print(fibonacci(7, 13))