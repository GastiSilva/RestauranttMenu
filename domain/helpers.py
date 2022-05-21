# the function give_amount returns a random value for the price
# the function give_time returns a random time
from random import randint


class Helpers:
    @classmethod
    def give_amount(cls):
        return randint(200, 1400)

    @classmethod
    def give_time(cls):
        return randint(10, 60)


