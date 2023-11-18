from abc import ABC

class Transport(ABC):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    def __str__(self):
        return f"Coordinates: {self.__coordinates}\nSpeed: {self.__speed}\nBrand: {self.__brand}\nYear: {self.__year}\nNumber: {self.__number}"

    def isInArea(self, pos_x: float, pos_y: float, length: float, width: float) -> bool:
        return pos_x < self.__coordinates[0] < pos_x + length and pos_y < self.__coordinates[0] < pos_y + width

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates: tuple):
        if not isinstance(coordinates, tuple) or len(coordinates) != 2:
            raise TypeError("Illegal type coordinates")
        elif not 0 < coordinates[0] < 1000:
            raise ValueError("Illegal value pos_x")
        elif not 0 < coordinates[1] < 1000:
            raise ValueError("Illegal value pos_y")
        else:
            self.__coordinates = coordinates

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if not isinstance(speed, int):
            raise TypeError("Illegal type - speed")
        elif not 0 < speed < 1000:
            raise ValueError("Illegal value - speed")
        else:
            self.__speed = speed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if not isinstance(brand, str):
            raise TypeError("Illegal type brand")
        else:
            self.__brand = brand

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("Illegal type - year")
        elif not 0 < year < 2024:
            raise ValueError("Illegal value - year")
        else:
            self.__year = year

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, str):
            raise TypeError("Illegal type - number")
        else:
            self.__number = number


class Passenger(ABC):
    def __init__(self, passengers_capacity: int, number_of_passengers: int):
        self.__passengers_capacity = passengers_capacity
        self.__number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity: int):
        if isinstance(passengers_capacity, int):
            raise TypeError("Illegal type - passengers_capacity")
        elif 0 > passengers_capacity:
            raise ValueError("Illegal value - passengers_capacity")
        else:
            self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers: int):
        if isinstance(number_of_passengers, int):
            raise ValueError("Illegal type - number_of_passengers")
        elif not 0 < number_of_passengers < 1000 or number_of_passengers < self.passengers_capacity:
            raise ValueError("Illegal value - number_of_passengers")
        else:
            self.__number_of_passengers = number_of_passengers


class Cargo(ABC):
    def __init__(self, carrying: int):
        self.__carrying = carrying

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying: int):
        if isinstance(carrying, int):
            raise TypeError("Illegal type - number_of_passengers")
        elif not 0 < carrying < 1000:
            raise ValueError("Illegal value - number_of_passengers")
        else:
            self.__carrying = carrying


class Auto(Transport):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str):
        super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str, port: str):
        super().__init__(coordinates, speed, brand, year, number)
        self.port = port

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port: str):
        if isinstance(port, str):
            raise TypeError("Illegal type - number_of_passengers")
        else:
            self.__port = port


class Car(Auto):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str):
        super().__init__(coordinates, speed, brand, year, number)


class Bus(Auto, Passenger):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str, passengers_capacity: int, number_of_passengers: int):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if isinstance(passengers_capacity, int):
            raise TypeError("Illegal type - passengers_capacity")
        elif not 0 < passengers_capacity < 350:
            raise ValueError("Illegal value - passengers_capacity")
        else:
            self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int):
            raise TypeError("Illegal type - number_of_passengers")
        elif number_of_passengers < self.passengers_capacity:
            raise ValueError("Illegal value - passengers_capacity")
        else:
            self.__number_of_passengers = number_of_passengers


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str, carrying: int):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Cargo.__init__(self, carrying)

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying: int):
        if isinstance(carrying, int):
            raise TypeError("Illegal type - number_of_passengers")
        elif 0 < carrying < 1500:
            raise ValueError("Illegal value - number_of_passengers")
        else:
            self.__carrying = carrying


class Boat(Ship):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str, port: str):
        super().__init__(coordinates, speed, brand, year, number, port)


class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Cargo.__init__(self, carrying)


class Plane(Transport):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str, height: int):
        Transport.__init__(self, coordinates, speed, brand, year, number)
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        if not isinstance(height, int):
            raise TypeError("Illegal type - height")
        elif not 0 < height < 10000:
            raise ValueError("Illegal value - height")
        else:
            self.__height = height


class Seaplane(Plane, Ship):
    def __init__(self, coordinates: tuple, speed: int, brand: str, year: int, number: str, height: int, port: str):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Ship.__init__(self, coordinates, speed, brand, year, number, port)