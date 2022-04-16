import os
import re


class RestaurantMenu:
    archive_route = 'carta.txt'

    @classmethod
    def add_food(cls, food):
        with open(cls.archive_route, 'a', encoding='utf-8') as archive:
            archive.write(f'ID: {food._food_id}\nFood: {food.name}, Amount: {food.amount}, Time: {food.time}\n')

    @classmethod
    def list_order(cls):
        if os.path.exists(cls.archive_route):
            with open(cls.archive_route, 'r', encoding='utf-8') as archive:
                print(archive.read())
        else:
            print('The order is empty please choose a food \n')

    @classmethod
    def remove_food(cls, food_id):
        with open(cls.archive_route, 'r', encoding='utf-8') as archive:
            data = archive.read()
        with open(cls.archive_route, 'w', encoding='utf-8') as archive:
            if re.search(re.escape(food_id), data) is not None:
                regex = r"ID:.*" + re.escape(food_id) + r".*\n" + r"Food:.*" + r".*\n"
                subst = ''
                result = re.sub(regex, subst, data, count=1)
                archive.write(result)

    @classmethod
    def remove_order(cls):
        if os.path.exists(cls.archive_route):
            os.remove(cls.archive_route)
            print('REQUEST REMOVE')
        else:
            print('The order does not exist')

