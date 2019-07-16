from abc import ABCMeta, abstractmethod


class CarFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_car(self, make, model):
        pass


class SedanFactory(CarFactory):

    def create_car(self, make, model):
        return Sedan(make, model)


class SUVFactory(CarFactory):

    def create_car(self, make, model):
        return SUV(make, model)


class Car(metaclass=ABCMeta):

    @abstractmethod
    def start_engine(self):
        pass


class Sedan(Car):

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(self.make + ' ' + self.model + ' engine started!')


class SUV(Car):

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(self.make + ' ' + self.model + ' engine started!')


if __name__ == '__main__':
    sedan_factory = SedanFactory()
    sedan = sedan_factory.create_car('Subaru', 'Legacy')
    sedan.start_engine()

    suv_factory = SUVFactory()
    suv = suv_factory.create_car('Lexus', 'LX570')
    suv.start_engine()

