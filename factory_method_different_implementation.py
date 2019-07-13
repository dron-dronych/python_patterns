class Tea:

    def __init__(self, color, structure):
        self.color = color
        self.structure = structure

    def __str__(self):
        return ' '.join([self.color, self.structure, 'tea'])


class TeaBoiler:

    def boil(self, tea, boil_type):
        boil_ = self._get_boil_type(boil_type)

        return boil_(tea)

    @classmethod
    def _get_boil_type(cls, boil_type):
        if boil_type == 'gas':
            return cls._boil_gas

        elif boil_type == 'electricity':
            return cls._electricity_boil

        else:
            raise ValueError(boil_type)

    @classmethod
    def _boil_gas(cls, tea):

        print('Gas: boiling {}'.format(tea))

    @classmethod
    def _electricity_boil(cls, tea):
        print('Electric kettle: boiling {}.'.format(tea))


if __name__ == '__main__':
    tea = Tea('green', 'leaves')
    boiler = TeaBoiler()
    boiler.boil(tea, 'gas')

    tea = Tea('black', 'granular')
    boiler.boil(tea, 'electricity')