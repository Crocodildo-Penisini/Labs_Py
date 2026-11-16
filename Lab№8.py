class Animal(object):
    def __init__(self):
        self.can_fly = False
        self.can_run = False

    def print_abilities(self):
        print(self.__class__.__name__)
        print('Can fly:', self.can_fly)
        print('Can run:', self.can_run)
        print()


class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.can_fly = True


class Horse(Animal):
    def __init__(self):
        super().__init__()
        self.can_run = True


class Pegasus(Horse, Bird):
    pass


def gen_init(cls):
    def init(self):
        print('Entered', cls.__name__, "constructor")
        super(cls, self).__init__()
        print('Quit', cls.__name__, "constructor")

    cls.__init__ = init
    return cls


@gen_init
class A(object):
    pass


@gen_init
class B(object):
    pass


@gen_init
class C(A, B):
    pass


@gen_init
class D(C, B):
    pass


@gen_init
class E(D):
    pass


class Vehicle:
    def __init__(self, name, price, speed, year):
        self.__name = name
        self.__price = price
        self.__speed = speed
        self.__year = year

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def info(self):
        return (f"{self.__class__.__name__}: {self.__name}, ціна: {self.__price}, "
                f"швидкість: {self.__speed} км/год, рік випуску: {self.__year}")


class Plane(Vehicle):
    def __init__(self, name, price, speed, year, height, passengers):
        super().__init__(name, price, speed, year)
        self.__height = height
        self.__passengers = passengers

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        self.__passengers = value

    def info(self):
        return (super().info() +
                f", висота: {self.__height} м, пасажирів: {self.__passengers}")


class Car(Vehicle):
    def __init__(self, name, price, speed, year):
        super().__init__(name, price, speed, year)


class Ship(Vehicle):
    def __init__(self, name, price, speed, year, passengers, port):
        super().__init__(name, price, speed, year)
        self.__passengers = passengers
        self.__port = port

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        self.__passengers = value

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        self.__port = value

    def info(self):
        return (super().info() +
                f", пасажирів: {self.__passengers}, порт приписки: {self.__port}")


class Fleet:
    def __init__(self):
        self.__items = []

    def add(self, vehicle):
        self.__items.append(vehicle)

    def show(self):
        if not self.__items:
            print("Список порожній")
        for v in self.__items:
            print(v.info())

    def find(self, attribute, value):
        result = []
        for v in self.__items:
            if hasattr(v, attribute) and getattr(v, attribute) == value:
                result.append(v)
        return result


def show_list(items):
    if not items:
        print("Нічого не знайдено")
    for v in items:
        print(v.info())


print(" === Приклад 1 ===")
Bird().print_abilities()
Horse().print_abilities()
Pegasus().print_abilities()

print("       === Приклад 2 ===")
print(E.__mro__)
obj = E()

print("\n       === Завдання 1. Транспортні засоби ===")
fleet = Fleet()
fleet.add(Plane("Boeing 737", 90000000, 840, 2015, 11000, 180))
fleet.add(Plane("Airbus A320", 85000000, 830, 2018, 11000, 150))
fleet.add(Car("Toyota Camry", 30000, 210, 2020))
fleet.add(Car("BMW X5", 70000, 250, 2018))
fleet.add(Ship("Queen Mary", 700000000, 55, 2004, 2600, "Саутгемптон"))
fleet.add(Ship("Harmony", 900000000, 40, 2016, 5400, "Одеса"))

print("\nУсі транспортні засоби:")
fleet.show()

print("\nПошук за роком випуску (2018):")
show_list(fleet.find("year", 2018))

print("\nПошук за портом приписки (Одеса):")
show_list(fleet.find("port", "Одеса"))

print("\nПошук за кількістю пасажирів (150):")
show_list(fleet.find("passengers", 150))

print("\nПошук за назвою (BMW X5):")
show_list(fleet.find("name", "BMW X5"))

print("\nЗміна параметрів через властивості:")
car = fleet.find("name", "Toyota Camry")[0]
print("Було:", car.info())
car.price = 32000
car.speed = 220
print("Стало:", car.info())
