# in the food class, we see the name, amount and
# time attributes (referring to the time it takes for the food to come out)

class Food:
    count = -1

    def __init__(self, name, amount, time):
        Food.count += 1
        self._food_id = Food.count
        self._name = name
        self._amount = amount
        self._time = time

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time
