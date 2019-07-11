from abc import ABCMeta, abstractmethod


class Car(metaclass=ABCMeta):
    @abstractmethod
    def start_engine(self):
        pass


class Subaru(Car):
    def start_engine(self):
        print('Subaru engine started!')


class Bmw(Car):
    def start_engine(self):
        print('BMW engine started!')


class Lexus(Car):
    def start_engine(self):
        print('Lexus engine started!')


class CarFactory:

    @classmethod
    def make_car(self, carname):
        return eval(carname.capitalize())()


if __name__ == '__main__':
    subaru = CarFactory.make_car('subaru')
    bmw = CarFactory.make_car('BMW')
    lexus = CarFactory.make_car('Lexus')

    subaru.start_engine()
    bmw.start_engine()
    lexus.start_engine()