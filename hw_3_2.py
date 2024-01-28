# Модуль 3. Друге завдання

import random, os

# The function generate random list numbers from min to max values


def get_numbers_ticket(min, max, quantity):
    numbers = set()
    if min >= 1 and max <= 1000 and min <= quantity <= max:
        while len(numbers) < quantity:
            x = random.randint(min, max)
            numbers.add(x)
    lst = list(numbers)
    lst.sort()
    return lst


# Test cases

os.system("cls")
print("The lucky numbers are:")

# Correct values

print(get_numbers_ticket(1, 36, 5))
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 1000, 10))

# Incorrect values

print(get_numbers_ticket(1, 10, 11))
print(get_numbers_ticket(0, 35, 5))
print(get_numbers_ticket(1, 1001, 10))
