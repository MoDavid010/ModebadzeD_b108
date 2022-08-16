# Предметная область – автосалон. Разработать класс CarDealership, описывающий работу автосалона.
# Разработать класс Car, автомобиль описывается следующими параметрами: уникальный идентификатор, марка автомобиля,
# страна-производитель, год выпуска, объем двигателя, стоимость.
# Разработать класс Lorry на базе класс Car, грузовик характеризуется: весовым ограничение перевозки.


from abc import ABCMeta, abstractmethod


class CarDealership(metaclass=ABCMeta):

    def __init__(self, id, mark, country, year, v, price):
        self.id = id
        self.mark = mark
        self.country = country
        self.year = year
        self.v = v
        self.price = price

    @abstractmethod
    def info(self):
        pass


class Car(CarDealership):
    def info(self):
        print(f"Машина\nid:{self.id}\n"
              f"Марка:{self.mark}\n"
              f"Страна-производитель: {self.country}\n"
              f"Год выпуска: {self.year}"
              f"\nОбъем двигателя: {self.v}"
              f"\nСтоимость: {self.price}")


class Lorry(Car):
    __slots__ = ('id', 'mark', 'country', 'year', 'v', 'price', 'ogr')

    def __init__(self, id, mark, country, year, v, price, ogr):
        super().__init__(id, mark, country, year, v, price)
        self.id = id
        self.mark = mark
        self.country = country
        self.year = year
        self.v = v
        self.price = price
        self.ogr = ogr

    def info(self):
        print(f"\nГрузовик\nid:{self.id}"
              f"\nМарка:{self.mark}\n"
              f"Страна-производитель: {self.country}\n"
              f"Год выпуска: {self.year}\n"
              f"Объем двигателя: {self.v}\n"
              f"Стоимость: {self.price}\n"
              f"Весовое ограничение "
              f"перевозки:{self.ogr}")


if __name__ == '__main__':
    car = Car('777', 'Mazda', 'Japan', '2009', '106', '300 000p')
    car.info()
    lorry = Lorry('2849', 'MAZ', 'Russia', '2012', '100л', '2 200 000p', '1000кг')
    lorry.info()



