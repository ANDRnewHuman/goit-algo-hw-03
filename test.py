'''
from datetime import datetime

def get_days_from_today(date):
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    
    current_date = datetime.today()
    
    delta = current_date - date_obj
    
    return delta.days


date = input("Enter date: \n")
days_difference = get_days_from_today(date)
print("Кількість днів між {} та сьогодні: {}".format(date, days_difference))

'''

from random import randint

def get_numbers_ticket(min, max, quantity):
    min = 1
    max = 49
    quantity = 6
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1) or min >= max:
        return []
    result_array = set()
    while len(result_array) < quantity:
        result_array.add(randint(min, max))
    return sorted(list(result_array))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
