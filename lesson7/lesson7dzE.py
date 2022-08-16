# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:
    def __init__(self, A, B, C):
        def side_length(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        self.A = A
        self.B = B
        self.C = C

        self.AB = side_length(self.A, self.B)
        self.BC = side_length(self.B, self.C)
        self.CA = side_length(self.C, self.A)

    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2

        return math.sqrt(
            semi_perimeter * (semi_perimeter - self.AB) * (semi_perimeter - self.BC) * (semi_perimeter - self.CA))

    def perimeterTriangle(self):
        return self.AB + self.BC + self.CA

    def heightTriangle(self):
        return self.areaTriangle() / (self.AB / 2)


triangle1 = Triangle((8, 13), (4, 9), (5, 2))

print(triangle1.areaTriangle())
print(triangle1.heightTriangle())
print(triangle1.perimeterTriangle())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezium:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def len_side(self):  # вычисление коодинат сторон трпеции

        ab = [self.b[0] - self.a[0], self.b[1] - self.a[1]]
        bc = [self.c[0] - self.b[0], self.c[1] - self.b[1]]
        cd = [self.d[0] - self.c[0], self.d[1] - self.c[1]]
        da = [self.a[0] - self.d[0], self.a[1] - self.d[1]]
        # вычисление длины сторон трапеции
        len_ab = math.sqrt(math.fabs(ab[0] ** 2 + ab[1] ** 2))
        len_bc = math.sqrt(math.fabs(bc[0] ** 2 + bc[1] ** 2))
        len_cd = math.sqrt(math.fabs(cd[0] ** 2 + cd[1] ** 2))
        len_da = math.sqrt(math.fabs(da[0] ** 2 + da[1] ** 2))

        return len_ab, len_bc, len_cd, len_da

    def check(self):
        return self.len_side()[0] == self.len_side()[2]

    def perimetr(self):
        p = 0
        for i in self.len_side():
            p += i
        return p

    def square(self):
        import math
        s = ((self.len_side()[1] + self.len_side()[3]) / 2) * math.sqrt(
            (self.len_side()[0] ** 2) - ((self.len_side()[3] - self.len_side()[1]) ** 2) / 4)
        return s


trapezium1 = Trapezium([1, 2], [3, 5], [4, 5], [6, 8])
print("Является ли трапеция равнобокой: {}".format(trapezium1.check()))
print("Периметр трапеции = {}".format(trapezium1.perimetr()))
print("Площадь трапеции = {}".format(trapezium1.square()))