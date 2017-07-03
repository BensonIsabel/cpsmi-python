class CarType:
    def __repr__(self):
        return self.__str__()


class SmallCar(CarType):
    def __str__(self):
        return 'SmallCar'


class Truck(CarType):
    def __str__(self):
        return 'Truck'


class Car:
    cartype = ''

    def __str__(self):
        return self.cartype.__str__()

    def __repr__(self):
        return self.cartype.__repr__()

    def set_cartype(self):
        raise AttributeError('Not Implemented car type')


class CarA(Car):
    def set_cartype(self):
        self.cartype = SmallCar()


class CarB(Car):
    def set_cartype(self):
        self.cartype = Truck()


class Parking:
    inside = []

    def drivein(self, auto: Car):
        self.inside.append(auto)

    def driveout(self, auto: Car):
        if auto in self.inside:
            self.inside.remove(auto)

    def kpp(self, auto: Car):
        print(str(auto), " trying to enter\n")
        if str(auto.cartype) == "SmallCar":
            self.drivein(auto)
            print(str(auto), " inside\n")
        else:
            print(str(auto), "Go away!\n")

    def __str__(self):
        s = "Now inside parking we have: \n" + str(self.inside)
        return s


c1 = CarA()
c1.set_cartype()
print(str(c1))

c2 = CarB()
c2.set_cartype()
print(str(c2))

parking = Parking()
parking.kpp(c1)
parking.kpp(c2)
print(str(parking))
