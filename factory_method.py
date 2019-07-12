from abc import ABCMeta, abstractmethod


class Door(metaclass=ABCMeta):

    @abstractmethod
    def has_window(self):
        pass


class SideDoor(Door):

    def has_window(self):
        return True


class BackDoor(Door):

    def has_window(self):
        return True


class Trunk(Door):

    def has_window(self):
        return False


class Car(metaclass=ABCMeta):

    def __init__(self):
        self.doors = []

    @abstractmethod
    def describe(self):
        pass

    def add_door(self, door):
        self.doors.append(door)

    def get_doors(self):
        return self.doors


class CargoCar(Car):

    def __init__(self):
        super().__init__()

        for i in range(0,4):
            self.add_door(SideDoor())

        self.add_door(Trunk())

    def describe(self):
        print('Cargo car!')


class Sedan(Car):

    def __init__(self):
        super().__init__()

        for i in range(0, 4):
            self.add_door(SideDoor())

        self.add_door(BackDoor())

    def describe(self):
        print('Sedan!')


if __name__ == '__main__':
    sedan = Sedan()
    sedan.describe()
    for door in sedan.get_doors():
        print(door.has_window())
