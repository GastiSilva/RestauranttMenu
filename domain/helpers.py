# the function returns a random value for the price
# the function returns a random time
from random import randint


class Helpers:
    @classmethod
    def give_amount(cls):
        return randint(200, 1300)

    @classmethod
    def give_time(cls):
        return randint(10, 60)







