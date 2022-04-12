# At the time of choosing the food in case of () write its name by keyboard
from domain.Food import Food
from service.RestaurantMenu import RestaurantMenu as rm
from domain.helpers import Helpers as helps

options = None
list_amount = []


while options != 6:
    print('1. Choose food ')
    print('2. See order')
    print('3. Remove food')
    print('4. See total amount')
    print('5. Remove order')
    print('6. Exit')
    options = int(input('Select an option: '))

    if options == 1:
        food_name = input('Choose food: ')
        food_amount = helps.give_amount()
        food_time = helps.give_time()
        food = Food(food_name, food_amount, food_time)
        rm.add_food(food)
        list_amount.insert(food.count, food_amount)
    elif options == 2:
        rm.list_order()
    elif options == 3:
        food = input('What food do you want to delete(id)? ')
        list_amount[int(food)] = 0
        rm.remove_food(food)
    elif options == 4:
        total_amount = 0
        for i in list_amount:
            total_amount += i
        print(f' The total amount of food is {total_amount} '.center(50, '-'))

    elif options == 5:
        rm.remove_order()


else:
    print(' ENJOY THE FOOD '.center(50, '-'))