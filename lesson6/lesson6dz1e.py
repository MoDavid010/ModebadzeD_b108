def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """

    return (a * b) ** 0.5


try:

    a = float(input("a = "))
    b = float(input("b = "))

    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError:
    print('Некоректный ввод')
