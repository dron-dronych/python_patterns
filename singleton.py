class Singleton:

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)

        return cls._instance


if __name__ == '__main__':
    singleton_1 = Singleton()
    singleton_2 = Singleton()

    print(singleton_1)
    print(singleton_2)



