# At the time of choosing the food in case of () write its name by keyboard
import os

from domain.Food import Food
from service.RestaurantMenu import RestaurantMenu as rm

options = None
list_amount = []
list_time = []

try:
    while options != 7:
        print('1. Choose food ')
        print('2. See order')
        print('3. Remove food')
        print('4. See total amount')
        print('5. See average time')
        print('6. Remove order')
        print('7. Finish order')
        options = int(input('Select an option: '))

        if options == 1:
            food_name = input('Choose food (wite the name if the food): ')
            food = Food(food_name)
            rm.add_food(food)
            list_amount.insert(food.count, food.amount)
            list_time.insert(food.count, food.time)

        elif options == 2:
            if os.stat('carta.txt').st_size == 0:
                print(f'The order is empty please choose a food \n'.center(20, '-'))
            else:
                rm.list_order()

        elif options == 3:
            if os.stat('carta.txt').st_size == 0:
                print(f'No food to remove'.center(20, '-'))
            else:
                food = input('What food do you want to delete(id)? ')
                list_amount[int(food)] = 0
                list_time[int(food)] = 0
                rm.remove_food(food)

        elif options == 4:
            total_amount = 0
            for i in list_amount:
                total_amount += i
            print(f' The total amount of food is {total_amount} '.center(50, '-'))

        elif options == 5:
            average_time = 0
            average_time_aux = 0
            for k in list_time:
                average_time_aux += k
            average_time = int(average_time_aux / len(list_time))
            print(f' The average time is {average_time} minutes'.center(50, '-'))

        elif options == 6:
            rm.remove_order()

    else:
        print(" thanks come back soon ".center(50, '-'))

except ZeroDivisionError as zde:
    print(f'ZeroDivisionError- Ocurrio un error: {type(zde)}')
except TypeError as te:
    print(f'TypeError- Ocurrio un error: {type(te)}')
except IndexError as ie:
    print(f'IndexError- Ocurrio un error: {type(ie)}')
except Exception as e:
    print(f'Exception- Ocurrio un error: {type(e)}')

finally:
    pass
